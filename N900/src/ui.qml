import QtQuick 1.0

Rectangle {
    id: base
    width: 800
    height: 420
    color: 'black'

    Image {
        id: playPauseButton
        width: 64
        height: 64
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        source: "playpause.png"

        MouseArea {
            width: parent.width
            height: parent.height
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            onClicked: {
                ui_backend.playPauseClicked()
            }
        }
    }
}
