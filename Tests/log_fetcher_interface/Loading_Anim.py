from pyqt_translucent_full_loading_screen_thread import LoadingThread, LoadingTranslucentScreen
from PyQt5.QtCore import QTimer



def StartLoading(self, message):
    self.__loadingTranslucentScreen = LoadingTranslucentScreen(parent=self, description_text=message)
    self.__loadingTranslucentScreen.setDescriptionLabelDirection('Right')
    self.__thread = LoadingThread(loading_screen=self.__loadingTranslucentScreen)
    self.__thread.start()
    QTimer.singleShot(1000, self.StopLoading)
    
    
def StopLoading(self):
    if self.__thread and self.__thread.isRunning():
        self.__thread.quit()  
        self.__thread.wait() 
        self.__loadingTranslucentScreen.stop()