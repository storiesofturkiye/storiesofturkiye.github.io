document.addEventListener('DOMContentLoaded', function() {
    const pageFlip = new St.PageFlip(
        document.getElementById("book"),
        {
            width: 550,
            height: 733,
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

    const pages = document.querySelectorAll(".page");
    pageFlip.loadFromHTML(pages);

    let isMuted = false;
    const muteBtn = document.getElementById('mute-btn');

    // Sesleri tamamen durduran yardımcı fonksiyon
    function stopAllAudio() {
        document.querySelectorAll('.page-audio').forEach(audio => {
            audio.pause();
            audio.currentTime = 0;
        });
    }

    // Mute butonu kontrolü
    muteBtn.addEventListener('click', () => {
        isMuted = !isMuted;
        muteBtn.innerText = isMuted ? "🔇 Sesi Aç" : "🔊 Sesi Kapat";
        if (isMuted) {
            stopAllAudio();
        } else {
            // Sesi geri açtığında o anki sayfayı oynatmayı dene
            const currentIndex = pageFlip.getCurrentPageIndex();
            playAudioForPage(currentIndex);
        }
    });

    function playAudioForPage(index) {
        if (isMuted) return;
        
        const currentPage = pages[index];
        if (currentPage) {
            const audio = currentPage.querySelector('.page-audio');
            if (audio) {
                audio.play().catch(err => console.log("Otomatik oynatma engellendi, etkileşim bekleniyor."));
            }
        }
    }

    // Sayfa çevrildiğinde tetiklenen olay
    pageFlip.on('flip', (e) => {
        stopAllAudio();
        playAudioForPage(e.data);
    });
});



function fitText(el) {
    let fontSize = 20; // başlangıç
    el.style.fontSize = fontSize + "px";

    while (el.scrollHeight > el.clientHeight && fontSize > 12) {
        fontSize--;
        el.style.fontSize = fontSize + "px";
    }
}

document.querySelectorAll(".page-text").forEach(el => {
    fitText(el);
});
