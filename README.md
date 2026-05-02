# Stories of Türkiye - Karamel's Books

Bu proje, Türkiye'nin kültürünü, tarihini, doğasını ve coğrafyasını anlatan 53 farklı hikaye kitabını çoklu dil desteğiyle sunan etkileşimli bir web platformudur. Ziyaretçiler, "Karamel" adlı karakterin rehberliğinde Türkiye'nin güzelliklerini keşfederler.

## Proje Hakkında
Web sitesi, 34 farklı dil seçeneği ile sunulan 53 adet hikaye kitabının merkezidir. Kullanıcılar ana sayfada bir dil seçtiğinde veya arama çubuğunu kullandığında, istedikleri kitaba hızlıca ulaşabilirler. Seçilen kitaplar, sayfa çevirme animasyonlarına sahip etkileşimli e-kitaplar (HTML/JS) olarak yeni bir sekmede açılır.

## Klasör ve Dosya Yapısı

Proje dizininde yer alan klasörler ve dosyaların görevleri aşağıda açıklanmıştır:

### Ana Dosya
- **`index.html`**: Web sitesinin kalbi olan ana sayfadır. Tüm 53 kitabın kapak görselleriyle birlikte listelendiği, **dil seçimi** (34 dil) ve **kitap arama** (search) işlevlerinin barındırıldığı dosyadır. Kullanıcı bir kitaba tıkladığında, `index.html` dosyasındaki JavaScript, kullanıcıyı seçili dile göre dinamik olarak ilgili kitabın bağlantısına (`./web/{Dil}/{KitapID}/index.html`) yönlendirir.

### Klasörler
- **`imgs/`**: Ana sayfada (`index.html`) sergilenen kitapların kapak görsellerini (`1.jpg`, `2.jpg` ... `53.jpg`) barındıran klasördür. Ayrıca site içinde kullanılan logo ve bazı grafik tasarımları (ör. `Houston logo.png`, `KARAMEL 4.png`) da bu klasörde yer alır.
- **`dil/`**: Projenin çok dilli yapısının temel kaynak klasörüdür. Desteklenen 34 farklı dil için (ör. `English`, `Turkish`, `Arabic`, `Spanish`) ayrı ayrı alt klasörler barındırır. Bu klasörler genellikle kitapların çevrilmiş metin dosyalarını organize etmek için kullanılır.
- **`main/`**: Etkileşimli e-kitapların üretilmesi için gereken ham materyalleri (orijinal sayfa görselleri vb.) ve Python otomasyon betiklerini (ör. `xx.py`) içeren kaynak dizinidir. İçerisinde 1'den 53'e kadar numaralandırılmış alt klasörler bulunur ve her biri bir kitabın temel görsellerini temsil eder.
- **`web/`**: Kullanıcılara sunulan **nihai, çalışır durumdaki etkileşimli e-kitapların** (HTML, CSS, JS ve resimler) bulunduğu ana çıktı klasörüdür. Yapısı dil ve kitap numarasına göre hiyerarşik olarak düzenlenmiştir (Örneğin: `web/English/1/index.html`). Kitap okuma deneyimi, sayfa çevirme animasyonları ve diğer işlevler tamamen bu klasör altındaki yapı tarafından sağlanır.

## Temel Özellikler
- **Kapsamlı Dil Desteği:** Ana sayfadaki açılır menü sayesinde aynı kütüphaneye saniyeler içinde 34 farklı dilde erişim imkanı.
- **Hızlı Arama:** İstenilen hikayeye anında ulaşabilmek için tasarlanmış anlık arama (search) kutusu.
- **Etkileşimli Okuma:** Sadece bir PDF veya düz metin yerine, kitap sayfası çevirme animasyonlarıyla desteklenen, çocuk dostu e-kitap altyapısı.
