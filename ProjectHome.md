# Wiki Loves Monuments 2011 dataset #

This is a dataset for [Wiki Loves Monuments 2011](http://commons.wikimedia.org/wiki/Commons:Wiki_Loves_Monuments_2011). It contains metadata of all the images uploaded to Wikimedia Commons from September 1 to September 30, 2011, during the Wiki Loves Monuments 2011 photo contest.

  * Article: "[Wiki Loves Monuments 2011: the experience in Spain and reflections regarding the diffusion of cultural heritage](http://digithum.uoc.edu/ojs/index.php/digithum/issue/view/n14)"

## Dataset structure ##
```
file_id|file_name|file_user_name|file_date_taken|file_date_upload|file_size|file_width|file_height|file_monument_id|file_country
16430663|File:0 Bergues - Beffroi (1).jpg|Jean-Pol GRANDMONT|2011-08-30T17:58:02Z|2011-09-11T11:30:44Z|2949829|2373|3560||fr
16604917|"File:""DINTR-UN LEMN"" MONASTERY 2.jpg"|Strainubot|2007-08-14T10:06:22Z|2011-09-20T21:16:03Z|2481893|2816|1584|VL-II-a-A-09742|ro
16416551|File:01 - Ambronay Abbaye .jpg|Thierry de Villepin|2011-08-08T15:59:01Z|2011-09-10T14:29:23Z|8365933|5184|3456|PA00116291|fr
16499008|File:'s Gravenvoeren (60).JPG|Basvb|2011-07-10T19:00:34Z|2011-09-15T17:38:52Z|4863766|3264|2448|37689|be
16594537|File:0 Bouillon - Remparts sud-est du château.JPG|Jean-Pol GRANDMONT|2008-06-30T12:51:01Z|2011-09-20T14:14:19Z|1616344|1288|1936||be
16509491|"File:""Русский Музей"", г.Санкт-Петербург.jpg"|Antonleto|2009-09-22T00:50:02Z|2011-09-16T10:51:23Z|3559611|3888|2592|7810526000|ru
16509495|"File:""Русский Музей"", картинный зал, г.Санкт-Петербург (2).jpg"|Antonleto|2009-09-22T01:21:06Z|2011-09-16T10:51:25Z|4248560|3888|2592|7810526000|ru
16633433|File:05.kaplica z 1848r w Łowiczu.jpg|Michalmarczyk|2011-09-21T15:35:24Z|2011-09-22T12:20:30Z|2409545|4000|3000|LD;128/571;Łowicz|pl
17149008|"File:""Halászlány"" kútszobor (4965. számú műemlék).jpg"|TgrBot|2011-07-25T15:44:08Z|2011-10-28T00:56:19Z|789238|1500|1117|4965|
```

## Usage examples ##

All the examples have been created using [wlm-2011-dataset-v1.zip](http://code.google.com/p/wlm-2011-dataset/downloads/detail?name=wlm-2011-dataset-v1.zip).


**Total images in September 2011**: `cut -d"|" -f5 table-files.csv | grep "2011-09-" -c`

Result: 163251

**Total images in September 2011 from Spain**: `grep "[^|]*|[^|]*|[^|]*|[^|]*|2011-09-" table-files.csv | cut -d"|" -f10 | grep "^es" -c`

Result: 16708

**Total bytes**: `grep "[^|]*|[^|]*|[^|]*|[^|]*|2011-09-" table-files.csv | awk -F"|" '{x += $6} END {print "sum: "x}'`

Result: 470084085543

**Ranking by day**: `grep "[^|]*|[^|]*|[^|]*|[^|]*|2011-09-" table-files.csv | cut -d"|" -f5 | cut -c-10 | sort | uniq -c | sort -n`

Result:
```
   1565 2011-09-02
   2221 2011-09-03
   2375 2011-09-01
   2859 2011-09-08
   2979 2011-09-06
   3053 2011-09-07
   3153 2011-09-09
   3349 2011-09-05
   3380 2011-09-14
   3479 2011-09-04
   3555 2011-09-10
   3603 2011-09-16
   3761 2011-09-13
   4076 2011-09-12
   4181 2011-09-20
   4314 2011-09-11
   4414 2011-09-22
   4661 2011-09-17
   4684 2011-09-21
   4780 2011-09-15
   4824 2011-09-23
   5104 2011-09-19
   6130 2011-09-24
   6646 2011-09-26
   7041 2011-09-18
   8175 2011-09-25
   9132 2011-09-27
  10385 2011-09-28
  13222 2011-09-29
  22150 2011-09-30
```

**Most photographed monuments**: `grep "[^|]*|[^|]*|[^|]*|[^|]*|2011-09-" table-files.csv | cut -d"|" -f9 | sort | uniq -c | sort -n | tail`

Result:
```
    249 71688
    251 PA00088714
    252 70427
    256 70107
    270 70237
    318 PA00086975;type=classé
    329 PA00086780
    412 70099
    415 PA00093999
  52536 
```

It is PA00093999 with more than 400 photographs, an abbey in Conques, France. See a gallery with [some photos](http://commons.wikimedia.org/wiki/Category:Abbatiale_Sainte-Foy_de_Conques) and the [official profile](http://www.culture.gouv.fr/public/mistral/merimee_fr?ACTION=CHERCHER&FIELD_1=REF&VALUE_1=PA00093999).

About 52536 has no info about the monument id.