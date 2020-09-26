from aqt import mw
from aqt import gui_hooks
from anki import hooks
from PyQt5 import QtDBus, QtCore

def setProgress():
    dueCardCount = len(mw.col.find_cards("is:due"))
    studiedCardCount = len(mw.col.find_cards("rated:1"))
    progress = studiedCardCount / (studiedCardCount + dueCardCount)

    interface = "com.canonical.Unity.LauncherEntry"
    bus = QtDBus.QDBusConnection.sessionBus()
    if not bus.isConnected():
        print("Not connected to dbus!")
    signal = QtDBus.QDBusMessage.createSignal("/", interface, "Update")
    signal << "application://net.ankiweb.Anki.desktop"
    qtDueCardCount = QtCore.QVariant(dueCardCount)
    qtDueCardCount.convert(QtCore.QVariant.LongLong)
    signal << {'count': qtDueCardCount, 'count-visible': True, 'progress': progress, 'progress-visible': True}
    bus.send(signal)

gui_hooks.main_window_did_init.append(setProgress)
gui_hooks.reviewer_will_end.append(setProgress)