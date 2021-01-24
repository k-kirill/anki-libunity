# anki_libunity
`anki_libunity` is an Anki add-on that shows the number of remaining cards to study and the correspondent progress bar at Anki launcher on your dock/panel using libunity specification.

It works only on Linux with the panels/docks that support libunity such as KDE Plasma or Dash to Dock extension for GNOME.

![](screenshot_launcher.png)

Also, it displays notifications when the number of cards to study increases. For example, when there are new due cards.

![](screenshot_notification.png)

## Install
Please check the official add-on web page: https://ankiweb.net/shared/info/901237400

## Configuration
If your Anki's desktop file is not named `net.ankiweb.Anki.desktop`, then please change the application name in the add-on's config. It is used to find the Anki launcher and the Anki icon (for notifications).