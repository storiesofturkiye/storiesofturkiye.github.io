document.addEventListener('DOMContentLoaded', function () {

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

    // 🔊 TÜM SESLERİ DURDUR
    function stopAllAudio() {
        document.querySelectorAll('.page-audio').forEach(audio => {
            audio.pause();
            audio.currentTime = 0;
        });
    }

    // 🔊 SAYFAYA GÖRE SES ÇAL
    function playAudioForPage(index) {
        if (isMuted) return;

        const currentPage = pages[index];
        if (currentPage) {
            const audio = currentPage.querySelector('.page-audio');
            if (audio) {
                audio.play().catch(() => {});
            }
        }
    }

    // 🔊 MUTE BUTONU
    muteBtn.addEventListener('click', () => {
        isMuted = !isMuted;
        muteBtn.innerText = isMuted ? "🔇 Sesi Aç" : "🔊 Sesi Kapat";

        if (isMuted) {
            stopAllAudio();
        } else {
            const currentIndex = pageFlip.getCurrentPageIndex();
            playAudioForPage(currentIndex);
        }
    });

    // 📝 YAZIYI OTOMATİK SIĞDIR
    function fitText(el) {
        let fontSize = 20;
        el.style.fontSize = fontSize + "px";

        while (el.scrollHeight > el.clientHeight && fontSize > 12) {
            fontSize--;
            el.style.fontSize = fontSize + "px";
        }
    }

    function applyFitText() {
        document.querySelectorAll(".page-text").forEach(el => {
            fitText(el);
        });
    }

    // 🔗 LİNK SENKRONLAMA
    function updateLinks() {
        document.querySelectorAll(".YzqVVZ").forEach(card => {
            const first = card.querySelector(".dynamic-book-link");
            const second = card.querySelector('a[aria-label="Listen Now"]');

            if (first && second) {
                second.href = first.href;
            }
        });
    }

    // 📖 SAYFA DEĞİŞİNCE
    pageFlip.on('flip', (e) => {
        stopAllAudio();
        playAudioForPage(e.data);

        setTimeout(() => {
            applyFitText();
            updateLinks();
        }, 100);
    });

    // 🌍 DİL / SELECT DEĞİŞİMİ
    document.addEventListener("change", function (e) {
        if (e.target.tagName === "SELECT") {
            setTimeout(() => {
                updateLinks();
                applyFitText();
            }, 300);
        }
    });

    // 👀 DOM DEĞİŞİMLERİNİ İZLE (Wix gibi dinamik sistemler için)
    const observer = new MutationObserver(() => {
        updateLinks();
    });

    observer.observe(document.body, {
        childList: true,
        subtree: true,
        attributes: true
    });

    // 🚀 İLK YÜKLEME
    setTimeout(() => {
        applyFitText();
        updateLinks();
    }, 300);

});

function updateLinks() {
    const cards = document.querySelectorAll(".YzqVVZ");

    cards.forEach(card => {
        const firstLink = card.querySelector(".dynamic-book-link");
        const listenBtn = card.querySelector('a[aria-label="Listen Now"]');

        if (firstLink && listenBtn) {
            listenBtn.href = firstLink.href;
        }
    });
}