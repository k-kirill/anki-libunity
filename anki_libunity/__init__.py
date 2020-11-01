from aqt import mw
from aqt import gui_hooks
from PyQt5 import QtDBus, QtCore


def set_progress():
    due_card_count = len(mw.col.find_cards("is:new or is:due"))
    studied_card_count = len(mw.col.find_cards("rated:1"))
    progress = studied_card_count / (studied_card_count + due_card_count)

    interface = "com.canonical.Unity.LauncherEntry"
    bus = QtDBus.QDBusConnection.sessionBus()
    if not bus.isConnected():
        print("Not connected to dbus!")
    signal = QtDBus.QDBusMessage.createSignal("/", interface, "Update")
    signal << "application://net.ankiweb.Anki.desktop"
    qt_due_card_count = QtCore.QVariant(due_card_count)
    qt_due_card_count.convert(QtCore.QVariant.LongLong)
    signal << {'count': qt_due_card_count, 'count-visible': True, 'progress': progress, 'progress-visible': True}
    bus.send(signal)


gui_hooks.collection_did_load.append(lambda _: set_progress())
gui_hooks.reviewer_did_show_question.append(lambda _: set_progress())
gui_hooks.reviewer_will_end.append(set_progress)
gui_hooks.sync_did_finish.append(set_progress)

