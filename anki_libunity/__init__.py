from aqt import mw
from aqt import gui_hooks
from PyQt5 import QtDBus, QtCore


def set_progress():
    due_card_count = len(mw.col.find_cards("is:new or is:due"))
    studied_card_count = len(mw.col.find_cards("rated:1"))
    divisor = studied_card_count + due_card_count
    if divisor == 0:
        progress = 1
    else:
        progress = studied_card_count / divisor
    signal = "Update"
    path = "/"
    interface = "com.canonical.Unity.LauncherEntry"
    bus = QtDBus.QDBusConnection.sessionBus()
    if not bus.isConnected():
        print("Not connected to dbus!")
    signal = QtDBus.QDBusMessage.createSignal(path, interface, signal)
    signal << "application://" + app_name + ".desktop"
    qt_due_card_count = QtCore.QVariant(due_card_count)
    qt_due_card_count.convert(QtCore.QVariant.LongLong)
    signal << {'count': qt_due_card_count, 'count-visible': True, 'progress': progress, 'progress-visible': True}
    bus.send(signal)


config = mw.addonManager.getConfig(__name__)
app_name = config['app_name']
gui_hooks.collection_did_load.append(lambda _: set_progress())
gui_hooks.reviewer_did_show_question.append(lambda _: set_progress())
gui_hooks.reviewer_will_end.append(set_progress)
gui_hooks.sync_did_finish.append(set_progress)
