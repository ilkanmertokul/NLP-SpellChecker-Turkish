# NLP-SpellChecker-Turkish

Developed to correct Turkish sentences written using English letters only. 
For example: if the input sentence is “beklenen olumlu tepkiyi alamadi”, the output sentence will be “beklenen olumlu tepkiyi alamadı”.
Note that “olumlu” could have been “ölümlü” but we did not choose it.

..

#About the structure:

Phyton used with the help of nltk library to do this project. There is a small dataset with 7k words
called 5.txt to do testing. You can switch to 95.txt which is way bigger dataset.
There are 20 sentence samples which are all in english letters, program finds occurences on all
possible sentences. Example :
Found total of 256 combinations of = - surlara dogru surdu -
Here are a few:
surlara doğru surdu
surlara doğru surdü
surlara doğru sürdu
surlara doğru sürdü
This program calculates all sentences for = unigram , bigram.
These are the words that has been tested:
![Ekran görüntüsü_20230102_161746](https://user-images.githubusercontent.com/61903795/210236609-f857d8c5-b191-48a1-9cf1-dde04a80a602.png)

#How?
At first, this program calculates all possible sequences recursively for interchangeable letters like ‘i’ to
‘ı’ or ‘o’ to ‘ö’.
Then we put all these possible sequences to ngram models to get highest possible one with ngram
probabilities.
Sample output from program (1gram):
Found total of 256 combinations of = - surlara dogru surdu -
Here are a few:
surlara doğru surdu
surlara doğru surdü
surlara doğru sürdu
surlara doğru sürdü
Calculating the most highly version...
Most probable sentence is
"surlara doğru sürdü"
With 4.574479298484037e-11 probability!
You should look at helperFunctions.py for function of getting probable sentences.

# unigram
Found total of 1024 combinations of = - cin seddi sinirina yaklastilar -
"çin seddi sınırına yaklaştılar"
With 1.6582281390642324e-14 probability!
Found total of 1024 combinations of = - baskentinin istedigi buydu -
"başkentinin istediği buydu"
With 9.80245563960865e-12 probability!
Found total of 128 combinations of = - guneye dogru ilerlediler -
"güneye doğru ilerlediler"
With 2.2872396492420184e-11 probability!
Found total of 512 combinations of = - uc tane asker cin'in hakimiydi -
"üç tane asker çin'in hakimiydi"
With 2.3311366283578064e-18 probability!
Found total of 2048 combinations of = - suslu manciniklari ogretti -
"süslü mancınıkları öğretti"
With 5.881473383765191e-12 probability!
Found total of 128 combinations of = - yapabilecek durumda degildi -
"yapabilecek durumda değildi"
With 2.6139881705623066e-11 probability!
Found total of 128 combinations of = - muhafiz kitasi oldu -
"muhafız kıtası oldu"
With 3.5288840302591144e-11 probability!
Found total of 256 combinations of = - surlara dogru surdu -
"surlara doğru sürdü"
With 4.574479298484037e-11 probability!
Found total of 2048 combinations of = - oldugu tartisma konusudur -
"olduğu tartışma konusudur"
With 6.46962072214171e-11 probability!
Found total of 256 combinations of = - celaleddin'in pesine dustu -
"celaleddin'in peşine düştü"
With 1.3069940852811533e-11 probability!
Found total of 128 combinations of = - ayrildigi haberini aldi -
"ayrıldığı haberini aldı"
With 2.940736691882595e-11 probability!
Found total of 512 combinations of = - hanedaninin tavrini unutmamisti -
"hanedanının tavrını unutmamıştı"
With 6.534970426405767e-12 probability!
Found total of 128 combinations of = - ele gecirmek konu oldu -
"ele geçirmek konu oldu"
With 1.8618701912300151e-13 probability!
Found total of 256 combinations of = - oncu birlik dayanmisti -
"öncü birlik dayanmıştı"
With 6.534970426405767e-12 probability!
Found total of 128 combinations of = - ilk kez gerceklesmisti -
"ilk kez gerçekleşmişti"
With 1.6337426066014418e-11 probability!
Found total of 64 combinations of = - cengiz han da ona katildi -
"cengiz han da ona katıldı"
With 4.556456921466896e-13 probability!
Found total of 64 combinations of = - sehri ele gecirdi -
"şehri ele geçirdi"
With 1.0978750316361688e-09 probability!
Found total of 128 combinations of = - yapabilecek durumda degildi -
"yapabilecek durumda değildi"
With 2.6139881705623066e-11 probability!
Found total of 1024 combinations of = - saldiri tuzagı kurmustu -
"saldırı tuzağı kurmuştu"
With 1.3069940852811533e-11 probability!
Found total of 128 combinations of = - duvarlari onune yıgdı -
"duvarları önüne yığdı"
With 6.534970426405767e-12 probability!

--

# bigram
Found total of 1024 combinations of = - cin seddi sinirina yaklastilar -
"cın seddı sınırına yaklastılar"
With 3.788343650099976e-14 probability!
Found total of 1024 combinations of = - baskentinin istedigi buydu -
"baskentının ıstedığı buydu"
With 8.586912273559945e-11 probability!
Found total of 128 combinations of = - guneye dogru ilerlediler -
"ğuneye doğru ılerledıler"
With 8.586912273559945e-11 probability!
Found total of 512 combinations of = - uc tane asker cin'in hakimiydi -
"uc tane asker cın'ın hakımıydı"
With 1.67132808092646e-17 probability!
Found total of 2048 combinations of = - suslu manciniklari ogretti -
"suslu mancınıkları oğrettı" 
With 8.586912273559945e-11 probability!
Found total of 128 combinations of = - yapabilecek durumda degildi -
"yapabılecek durumda değıldı"
With 8.586912273559945e-11 probability!
Found total of 128 combinations of = - muhafiz kitasi oldu -
"muhafız kıtası oldu"
With 8.586912273559945e-11 probability!
Found total of 256 combinations of = - surlara dogru surdu -
"surlara doğru surdu"
With 8.586912273559945e-11 probability!
Found total of 2048 combinations of = - oldugu tartisma konusudur -
"olduğu tartısma konusudur"
With 8.586912273559945e-11 probability!
Found total of 256 combinations of = - celaleddin'in pesine dustu -
"celaleddın'ın pesıne dustu"
With 8.586912273559945e-11 probability!
Found total of 128 combinations of = - ayrildigi haberini aldi -
"ayrıldığı haberını aldı"
With 8.586912273559945e-11 probability!
Found total of 512 combinations of = - hanedaninin tavrini unutmamisti -
"hanedanının tavrını unutmamıstı"
With 8.586912273559945e-11 probability!
Found total of 128 combinations of = - ele gecirmek konu oldu -
"ele ğecırmek konu oldu"
With 3.788343650099976e-14 probability!
Found total of 256 combinations of = - oncu birlik dayanmisti -
"oncu bırlık dayanmıstı"
With 8.586912273559945e-11 probability!
Found total of 128 combinations of = - ilk kez gerceklesmisti -
"ılk kez ğerceklesmıstı"
With 8.586912273559945e-11 probability!
Found total of 64 combinations of = - cengiz han da ona katildi -
"cenğız han da ona katıldı"
With 1.67132808092646e-17 probability!
Found total of 64 combinations of = - sehri ele gecirdi -
"sehrı ele ğecırdı"
With 8.586912273559945e-11 probability!
Found total of 128 combinations of = - yapabilecek durumda degildi -
"yapabılecek durumda değıldı"
With 8.586912273559945e-11 probability!
Found total of 1024 combinations of = - saldiri tuzagı kurmustu -
"saldırı tuzağı kurmustu"
With 8.586912273559945e-11 probability!
Found total of 128 combinations of = - duvarlari onune yıgdı -
"duvarları onune yığdı"
With 8.586912273559945e-11 probability!
#Result
##Why unigram results are wonderful, but bigram is terrible?
Unigram is tested with a really small dataset, but bigram is tested with even smaller dataset. This
results really high count of zero probabilities, and it is still really bad eventhough i used a smoothing.
Unigram works good in small sets. If we had a million word corpora, bigram would perform better. If
we had even bigger corpora (trillions), trigram would have been better (ignoring memory – time
consuming facts).
Thans for reading.
İlkan Mert Okul, 1801042649




