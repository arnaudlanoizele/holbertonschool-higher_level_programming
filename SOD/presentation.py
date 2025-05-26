from gtts import gTTS

text = """
THE HISTORY OF MANGA IMPORTATION IN FRANCE

🇯🇵🇫🇷 Introduction: The Meeting of Two Cultures
The story of how manga came to France is the result of a long cultural journey, which began well before Japanese comic books started filling French bookstores. Between a fascination with Japanese animation, the bold initiatives of passionate publishers, and a growing curiosity from the public, France gradually became one of the world’s leading centers of “manga fandom.” Today, manga holds a prominent place in French pop culture, alongside Franco-Belgian comics and American superheroes. But how did this passion begin? To understand it, we have to go back to the first broadcasts of Japanese animated series on French television in the 1970s...

🌀 1. Before Manga: Japanese Anime in France (1970s–1980s)
In 1978, the anime "Goldorak" (UFO Robot Grendizer) was broadcast in France on Récré A2 (Antenne 2).


It was followed by Candy, Albator, Captain Future, Saint Seiya, Dragon Ball, etc.


These "Japanese cartoons" were hugely popular with children.


At that time, the term manga was not widely known in France.



📖 2. The First Manga Arrivals (1980s–1990s)
✍️ Early Attempts (1980s)
Magazines like Le Cri qui tue (1978–1981) published excerpts from Japanese manga (Tezuka, Ishinomori...), but without much commercial success.


🚀 The Key Role of Jacques Glénat
In the late 1980s, French publisher Jacques Glénat traveled to Japan to promote Franco-Belgian comics.


Instead, he discovered Akira by Katsuhiro Otomo at Kodansha and was impressed by its quality.


He secured the rights and published Akira in France in 1990, marking the first major manga success in the country.


He later obtained the rights to Dragon Ball, which became a massive hit.



📈 3. The Manga Boom in France (1990s–2000s)
Other publishers joined the market: Kana, Pika, Tonkam, Panini...


Major titles emerged:
 Sailor Moon, City Hunter, Ranma ½, Gunnm, Love Hina, Naruto, One Piece, Bleach...


Manga began to be published in the original right-to-left format, which preserved the authentic Japanese style.


"Manga" became a common word in French culture.


Bookstores created entire manga sections.



🎌 4. Cultural Acceptance and Recognition (2000s–Today)
Manga is now recognized as a legitimate storytelling and artistic form.


A wide variety of genres are available: shônen, shôjo, seinen, josei, yaoi, etc.


France became the 2nd largest manga market in the world, after Japan.


Events like Japan Expo (founded in 1999) attract hundreds of thousands of fans every year.


Japanese artists are now regularly invited to France.



🔍 Why Was Manga So Successful in France?
A strong tradition of comic book reading (Tintin, Astérix…).


Long-standing interest in Japanese culture.


Universal themes and relatable characters in manga stories.


Affordable pricing compared to traditional European comics.



🔚 Conclusion
The importation of manga in France was the result of cultural curiosity, key editorial decisions (especially by Jacques Glénat), and a generation of readers ready to embrace something new. Today, manga is deeply embedded in French pop culture.
📺 CLUB DOROTHÉE – SUMMARY HISTORY

🎬 1. What Was Club Dorothée?
Club Dorothée was a French children's TV show broadcast on TF1 from 1987 to 1997.
 It was hosted by Dorothée (real name: Frédérique Hoschedé) and her team (Ariane, Jacky, Corbier, Patrick).
 It became an iconic program that influenced an entire generation of French kids.

🗓️ 2. Key Dates
September 2, 1987: First broadcast of Club Dorothée on TF1.


August 1997: Final episode, marking 10 years of broadcasting.



📚 3. What Did the Show Offer?
Japanese anime (cartoons): The show is best known for airing series like Dragon Ball, Saint Seiya, Fist of the North Star, Sailor Moon, Maison Ikkoku, etc.


Live-action Japanese shows: Bioman, X-Or, San Ku Kaï...


Games, comedy, music, and variety segments: Dorothée and her team performed sketches, sang songs, and interacted with the kids.



🚨 4. Controversies
The show faced strong criticism in the 1990s:


It was accused of showing violent content to children.


Shows like Fist of the North Star and Dragon Ball Z were frequently targeted by parents and media.


Despite this, audiences remained very high.



📉 5. Why Did It End?
In 1997, TF1 chose not to renew its contract with the show's production company (AB Productions).


Club Dorothée was replaced by more “family-friendly” programming like TF! Jeunesse.



🌟 6. Legacy
Club Dorothée introduced a whole generation to Japanese animation and paved the way for manga culture in France.


It played a key role in making France the largest consumer of Japanese anime and manga outside of Japan.


Even today, the show is remembered fondly and with nostalgia by many adults.


🏁 Conclusion
The story of manga’s arrival in France perfectly illustrates how a foreign cultural form can, in just a few decades, become a central part of a nation’s cultural landscape. From the first anime broadcasts in the 1970s to the massive popularity of printed manga in the 1990s, through the controversies of Club Dorothée and the rise of events like Japan Expo, France has embraced, adapted, and celebrated this art form from Japan. Today, manga is no longer a passing trend—it is a vital part of everyday life for millions of French readers. This success stems from a unique combination of comic book heritage, a passion for imagination, and an openness to cultural diversity.

"""

tts = gTTS(text, lang='en' )
tts.save("presentation_english.mp3")

print("File ssaved as presentation_english.mp3")
