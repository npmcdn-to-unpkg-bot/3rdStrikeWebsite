function zoomImage(img) {
        var image = document.getElementById(img);
        image.style.height = "360px"
        image.style.width = "480px";
        image.style.position = "relative";
        image.style.left = "0px";
        image.style.top = "0px";
        image.style.zIndex = "1";
        image.style.paddingLeft = "5px";
    }
    function reduceImage(img) {
        var image = document.getElementById(img);
        image.style.height = "75%";
        image.style.width = "75%"
        // image.style.position = "relative";
        image.style.zIndex = "0";
    }