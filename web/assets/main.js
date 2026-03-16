document.addEventListener('DOMContentLoaded', function() {
    const pageFlip = new St.PageFlip(
        document.getElementById("book"),
        {
            width: 550, // base page width
            height: 733, // base page height
            size: "stretch",
            minWidth: 315,
            maxWidth: 1000,
            minHeight: 420,
            maxHeight: 1350,
            maxShadowOpacity: 0.5,
            showCover: true,
            mobileScrollSupport: false
        }
    );

    pageFlip.loadFromHTML(document.querySelectorAll(".page"));
});
