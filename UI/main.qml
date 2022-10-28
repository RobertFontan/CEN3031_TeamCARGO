import QtQuick
import QtQuick.Controls.Basic

ApplicationWindow {
    visible: true
    width: 600
    height: 500
    title: "Encyclomedia"   
    
    // Text {
    //     anchors.centerIn: parent
    //     text: "test :p "
    //     font.pixelSize: 24
    // }

    Image {
        
            id: bookshelf
            anchors.fill: parent
            source: "./image/bookshelf.jpg"
            opacity: 1
            z: -1
    }

    //Shelf{
        // have covers
        // some type of scrolling
    //}

    Favorite-Shelf {
        
    }


    
}