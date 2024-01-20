import asyncio
import os
import sys
from pathlib import Path

import qdarkstyle
import YtDlp

from qasync import QEventLoop, QApplication, asyncClose, asyncSlot
from PySide6.QtCore import QUrl, Qt, Slot
from PySide6.QtGui import QPixmap
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PySide6.QtWidgets import QMainWindow, QFileDialog
from ui_mainwindow import Ui_MainWindow
from urllib.parse import urlparse


def is_valid_url(value):
    try:
        result = urlparse(value)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ytdlp = YtDlp.YtDlpWrapper()
        self.thumbnail = QPixmap()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.chkSaveThumbnail.setVisible(False)
        self.ui.lblDuration.setVisible(False)

        self.manager = QNetworkAccessManager()
        self.manager.finished.connect(self.handle_thumbnail_finished)

        if getattr(sys, 'frozen', False):
            self.application_path = os.path.dirname(sys.executable)
        elif __file__:
            self.application_path = os.path.dirname(__file__)

    @asyncClose
    async def closeEvent(self, event):
        pass

    @asyncSlot()
    async def process_button_clicked(self):
        await self.ytdlp.get_info(self.ui.txtUrl.text())

        self.manager.get(QNetworkRequest(QUrl(self.ytdlp.video.thumbnail)))

        self.ui.txtVideoTitle.setText(self.ytdlp.video.title)
        self.ui.lblDuration.setText(self.ytdlp.video.duration)
        self.ui.lblDuration.adjustSize()
        self.ui.lblDuration.move(
            self.ui.imgThumbnail.width() - self.ui.lblDuration.width() - 1,
            self.ui.imgThumbnail.height() - self.ui.lblDuration.height() - 2
        )
        self.ui.txtVideoDescription.setPlainText(self.ytdlp.video.description)

        self.ui.txtOutputFilename.setText(
            f"{self.application_path}{os.sep}{self.ytdlp.video.filename}"
        )

        self.ui.cmbVideoFormats.clear()
        self.ui.cmbAudioFormats.clear()
        for f in reversed(self.ytdlp.video.video_formats):
            self.ui.cmbVideoFormats.addItem(
                f"{f['resolution']} - {f['vcodec']} - {f['ext']}",
                f['format_id']
            )

        for f in reversed(self.ytdlp.video.audio_formats):
            self.ui.cmbAudioFormats.addItem(
                f"{f['asr']}hz - {f['acodec']} - {f['ext']}",
                f['format_id']
            )

        self.ui.txtOutputFilename.setEnabled(True)
        self.ui.btnBrowse.setEnabled(True)
        self.ui.btnDownload.setEnabled(True)

    @Slot(str)
    def url_text_changed(self, value):
        if is_valid_url(value):
            self.ui.btnProcess.setEnabled(True)
        else:
            self.ui.btnProcess.setEnabled(False)

    @Slot()
    def browse_button_clicked(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")

        if directory:
            self.ui.txtOutputFilename.setText(
                f"{os.path.normpath(directory)}{os.sep}{self.ytdlp.video.filename}"
            )

    @Slot(int)
    def video_format_changed(self, index):
        if self.ui.cmbVideoFormats.currentData() is None or self.ui.chkQuality.isChecked():
            return

        filename = Path(self.ui.txtOutputFilename.text()).stem

        for item in self.ytdlp.video.video_formats:
            if item["format_id"] == self.ui.cmbVideoFormats.itemData(index):
                filename += f".{item['ext']}"
                break

        directory = os.path.dirname(self.ui.txtOutputFilename.text())

        self.ui.txtOutputFilename.setText(
            f"{directory}{os.sep}{filename}"
        )

    def handle_thumbnail_finished(self, reply):
        self.thumbnail.loadFromData(reply.readAll())
        self.ui.imgThumbnail.setPixmap(
            self.thumbnail.scaled(self.ui.imgThumbnail.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )

        self.ui.chkSaveThumbnail.setVisible(True)
        self.ui.lblDuration.setVisible(True)

    @Slot(bool)
    def quality_toggled(self, checked):
        if not checked:
            self.ui.cmbVideoFormats.setEnabled(True)
            self.ui.cmbAudioFormats.setEnabled(True)
        else:
            self.ui.cmbVideoFormats.setEnabled(False)
            self.ui.cmbAudioFormats.setEnabled(False)

            self.ui.txtOutputFilename.setText(
                f"{self.application_path}{os.sep}{self.ytdlp.video.filename}"
            )

    @asyncSlot()
    async def download_button_clicked(self):
        if self.ui.chkQuality.isChecked():
            await self.ytdlp.download(
                self.ui.txtUrl.text(),
                self.ui.txtOutputFilename.text()
            )
        else:
            await self.ytdlp.download(
                self.ui.txtUrl.text(),
                self.ui.txtOutputFilename.text(),
                f"{self.ui.cmbVideoFormats.currentData()}+{self.ui.cmbAudioFormats.currentData()}"
            )

        if self.ui.chkSaveThumbnail.isChecked():
            self.thumbnail.save(
                f"{os.path.dirname(self.ui.txtOutputFilename.text())}{os.sep}{self.ytdlp.video.title}.png",
                "PNG"
            )

        self.ui.chkSaveThumbnail.setVisible(False)
        self.ui.lblDuration.setVisible(False)
        self.ui.imgThumbnail.clear()
        self.ui.txtVideoTitle.clear()
        self.ui.txtVideoDescription.clear()
        self.ui.txtOutputFilename.clear()
        self.ui.cmbVideoFormats.clear()
        self.ui.cmbAudioFormats.clear()
        self.ui.txtOutputFilename.setEnabled(False)
        self.ui.btnBrowse.setEnabled(False)
        self.ui.btnDownload.setEnabled(False)

    @asyncSlot()
    async def download_video_button_clicked(self):
        if self.ui.chkQuality.isChecked():
            await self.ytdlp.download_format(
                self.ui.txtUrl.text(),
                "bestvideo"
            )
        else:
            await self.ytdlp.download_format(
                self.ui.txtUrl.text(),
                self.ui.cmbVideoFormats.currentData()
            )

    @asyncSlot()
    async def download_audio_button_clicked(self):
        if self.ui.chkQuality.isChecked():
            await self.ytdlp.download_format(
                self.ui.txtUrl.text(),
                "bestaudio"
            )
        else:
            await self.ytdlp.download_format(
                self.ui.txtUrl.text(),
                self.ui.cmbAudioFormats.currentData()
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    app_close_event = asyncio.Event()
    app.aboutToQuit.connect(app_close_event.set)

    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6'))

    window.show()

    with loop:
        loop.run_until_complete(app_close_event.wait())
