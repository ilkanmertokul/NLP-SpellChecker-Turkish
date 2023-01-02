# NLP-SpellChecker-Turkish

Developed to correct Turkish sentences written using English letters only. 
For example: if the input sentence is “beklenen olumlu tepkiyi alamadi”, the output sentence will be “beklenen olumlu tepkiyi alamadı”.
Note that “olumlu” could have been “ölümlü” but we did not choose it.

..

# About the structure:

Phyton used with the help of nltk library to do this project. There is a small dataset with 7k words
called 5.txt to do testing. You can switch to 95.txt which is way bigger dataset.<br />
There are 20 sentence samples which are all in english letters, program finds occurences on all
possible sentences. Example :<br />
Found total of 256 combinations of = - surlara dogru surdu -<br />
Here are a few:<br />
surlara doğru surdu<br />
surlara doğru surdü<br />
surlara doğru sürdu<br />
surlara doğru sürdü<br />
This program calculates all sentences for = unigram , bigram.<br />
These are the words that has been tested:<br />
![Ekran görüntüsü_20230102_161746](https://user-images.githubusercontent.com/61903795/210236609-f857d8c5-b191-48a1-9cf1-dde04a80a602.png)

# How?
At first, this program calculates all possible sequences recursively for interchangeable letters like ‘i’ to
‘ı’ or ‘o’ to ‘ö’.<br />
Then we put all these possible sequences to ngram models to get highest possible one with ngram
probabilities.<br />
Sample output from program (1gram):<br />
Found total of 256 combinations of = - surlara dogru surdu -<br />
Here are a few:<br />
surlara doğru surdu<br />
surlara doğru surdü<br />
surlara doğru sürdu<br />
surlara doğru sürdü<br />
Calculating the most highly version...<br />
Most probable sentence is<br />
"surlara doğru sürdü"<br />
With 4.574479298484037e-11 probability!<br />
You should look at helperFunctions.py for function of getting probable sentences.<br />

# unigram
Found total of 1024 combinations of = - cin seddi sinirina yaklastilar -<br />
"çin seddi sınırına yaklaştılar"<br />
With 1.6582281390642324e-14 probability!<br /><br />
Found total of 1024 combinations of = - baskentinin istedigi buydu -<br />
"başkentinin istediği buydu"<br />
With 9.80245563960865e-12 probability!<br /><br />
Found total of 128 combinations of = - guneye dogru ilerlediler -<br />
"güneye doğru ilerlediler"<br />
With 2.2872396492420184e-11 probability!<br /><br />
Found total of 512 combinations of = - uc tane asker cin'in hakimiydi -<br />
"üç tane asker çin'in hakimiydi"<br />
With 2.3311366283578064e-18 probability!<br /><br />
Found total of 2048 combinations of = - suslu manciniklari ogretti -<br />
"süslü mancınıkları öğretti"<br />
With 5.881473383765191e-12 probability!<br /><br />
Found total of 128 combinations of = - yapabilecek durumda degildi -<br />
"yapabilecek durumda değildi"<br />
With 2.6139881705623066e-11 probability!<br /><br />
Found total of 128 combinations of = - muhafiz kitasi oldu -<br />
"muhafız kıtası oldu"<br />
With 3.5288840302591144e-11 probability!<br /><br />
Found total of 256 combinations of = - surlara dogru surdu -<br />
"surlara doğru sürdü"<br />
With 4.574479298484037e-11 probability!<br /><br />
Found total of 2048 combinations of = - oldugu tartisma konusudur -<br />
"olduğu tartışma konusudur"<br />
With 6.46962072214171e-11 probability!<br /><br />
Found total of 256 combinations of = - celaleddin'in pesine dustu -<br />
"celaleddin'in peşine düştü"<br />
With 1.3069940852811533e-11 probability!<br /><br />
Found total of 128 combinations of = - ayrildigi haberini aldi -<br />
"ayrıldığı haberini aldı"<br />
With 2.940736691882595e-11 probability!<br /><br />
Found total of 512 combinations of = - hanedaninin tavrini unutmamisti -<br />
"hanedanının tavrını unutmamıştı"<br />
With 6.534970426405767e-12 probability!<br /><br />
Found total of 128 combinations of = - ele gecirmek konu oldu -<br />
"ele geçirmek konu oldu"<br />
With 1.8618701912300151e-13 probability!<br /><br />
Found total of 256 combinations of = - oncu birlik dayanmisti -<br />
"öncü birlik dayanmıştı"<br />
With 6.534970426405767e-12 probability!<br /><br />
Found total of 128 combinations of = - ilk kez gerceklesmisti -<br />
"ilk kez gerçekleşmişti"<br />
With 1.6337426066014418e-11 probability!<br /><br />
Found total of 64 combinations of = - cengiz han da ona katildi -<br />
"cengiz han da ona katıldı"<br />
With 4.556456921466896e-13 probability!<br /><br />
Found total of 64 combinations of = - sehri ele gecirdi -<br />
"şehri ele geçirdi"<br />
With 1.0978750316361688e-09 probability!<br /><br />
Found total of 128 combinations of = - yapabilecek durumda degildi -<br />
"yapabilecek durumda değildi"<br />
With 2.6139881705623066e-11 probability!<br /><br />
Found total of 1024 combinations of = - saldiri tuzagı kurmustu -<br />
"saldırı tuzağı kurmuştu"<br />
With 1.3069940852811533e-11 probability!<br /><br />
Found total of 128 combinations of = - duvarlari onune yıgdı -<br />
"duvarları önüne yığdı"<br />
With 6.534970426405767e-12 probability!<br />

--

# bigram
Found total of 1024 combinations of = - cin seddi sinirina yaklastilar -<br />
"cın seddı sınırına yaklastılar"<br />
With 3.788343650099976e-14 probability!<br /><br />
Found total of 1024 combinations of = - baskentinin istedigi buydu -<br />
"baskentının ıstedığı buydu"<br />
With 8.586912273559945e-11 probability!<br /><br />
Found total of 128 combinations of = - guneye dogru ilerlediler -<br />
"ğuneye doğru ılerledıler"<br />
With 8.586912273559945e-11 probability!<br /><br />
Found total of 512 combinations of = - uc tane asker cin'in hakimiydi -<br />
"uc tane asker cın'ın hakımıydı"<br />
With 1.67132808092646e-17 probability!<br /><br />
Found total of 2048 combinations of = - suslu manciniklari ogretti -<br />
"suslu mancınıkları oğrettı" <br />
With 8.586912273559945e-11 probability!<br /><br />
Found total of 128 combinations of = - yapabilecek durumda degildi -<br />
"yapabılecek durumda değıldı"<br />
With 8.586912273559945e-11 probability!<br /><br />
Found total of 128 combinations of = - muhafiz kitasi oldu -<br />
"muhafız kıtası oldu"<br />
With 8.586912273559945e-11 probability!<br /><br />
Found total of 256 combinations of = - surlara dogru surdu -<br />
"surlara doğru surdu"<br />
With 8.586912273559945e-11 probability!<br /><br />
Found total of 2048 combinations of = - oldugu tartisma konusudur -<br />
"olduğu tartısma konusudur"<br />
With 8.586912273559945e-11 probability!<br /><br />
Found total of 256 combinations of = - celaleddin'in pesine dustu -<br />
"celaleddın'ın pesıne dustu"<br />
With 8.586912273559945e-11 probability!<br /><br />
Found total of 128 combinations of = - ayrildigi haberini aldi -<br />
"ayrıldığı haberını aldı"<br />
With 8.586912273559945e-11 probability!<br /><br />
Found total of 512 combinations of = - hanedaninin tavrini unutmamisti -<br />
"hanedanının tavrını unutmamıstı"<br />
With 8.586912273559945e-11 probability!<br /><br />
Found total of 128 combinations of = - ele gecirmek konu oldu -<br />
"ele ğecırmek konu oldu"<br />
With 3.788343650099976e-14 probability!<br /><br />
Found total of 256 combinations of = - oncu birlik dayanmisti -<br />
"oncu bırlık dayanmıstı"<br />
With 8.586912273559945e-11 probability!<br /><br />
Found total of 128 combinations of = - ilk kez gerceklesmisti -<br />
"ılk kez ğerceklesmıstı"<br />
With 8.586912273559945e-11 probability!<br /><br />
Found total of 64 combinations of = - cengiz han da ona katildi -<br />
"cenğız han da ona katıldı"<br />
With 1.67132808092646e-17 probability!<br /><br />
Found total of 64 combinations of = - sehri ele gecirdi -<br />
"sehrı ele ğecırdı"<br />
With 8.586912273559945e-11 probability!<br /><br />
Found total of 128 combinations of = - yapabilecek durumda degildi -<br />
"yapabılecek durumda değıldı"<br />
With 8.586912273559945e-11 probability!<br /><br />
Found total of 1024 combinations of = - saldiri tuzagı kurmustu -<br />
"saldırı tuzağı kurmustu"<br />
With 8.586912273559945e-11 probability!<br /><br />
Found total of 128 combinations of = - duvarlari onune yıgdı -<br />
"duvarları onune yığdı"<br />
With 8.586912273559945e-11 probability!<br /><br />
# Result
## Why unigram results are wonderful, but bigram is terrible?
Unigram is tested with a really small dataset, but bigram is tested with even smaller dataset. This
results really high count of zero probabilities, and it is still really bad eventhough i used a smoothing.
Unigram works good in small sets. If we had a million word corpora, bigram would perform better. If
we had even bigger corpora (trillions), trigram would have been better (ignoring memory – time
consuming facts).<br />
Thans for reading.<br />
İlkan Mert Okul.




