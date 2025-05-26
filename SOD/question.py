from gtts import gTTS

text = """
Introduction
✅ 1. What is manga?
A manga is a Japanese comic book.
✅ 2. How did Japanese and French cultures first connect through manga?
Jacques Glénat, a French publisher, went to Japan. There, he discovered the manga Akira by Katsuhiro Otomo at Kodansha. He decided to publish it in France.
✅ 3. Why is France important in the world of manga today?
France is the second biggest manga market in the world, after Japan. Manga is very popular in French culture. Many bookstores have big manga sections, and events like Japan Expo attract thousands of fans every year.

🌀 1. Before Manga: Japanese Anime in France
✅ 4. When was Japanese anime first shown on French TV?
The first anime on French TV was Goldorak (UFO Robot Grendizer) in 1978.
✅ 5. What was the name of the first popular anime in France?
The first popular anime in France was Goldorak.
✅ 6. Were French people familiar with the word “manga” at that time?
No, French people didn’t know the word “manga” at that time.
Why didn’t French people know the word “manga” at the beginning?
In the 1970s and 1980s, Japanese comics were not well known in France. People only saw Japanese cartoons on TV, but they did not know the word “manga.”
Also, the first manga books were often changed or translated without keeping the original Japanese style or name. So, French readers did not know the word “manga.”
It was only in the 1990s, when publishers like Jacques Glénat started to publish manga in the original format and use the word “manga,” that people in France learned and used the word.
📖 2. The First Manga Arrivals
✅ 7. What were the first attempts to bring manga to France?
The first attempts to bring manga to France were made by magazines like Le Cri qui Tue. They published short parts of Japanese manga, but it was not very successful at that time.

✅ 8. Who is Jacques Glénat?
Jacques Glénat is a famous French publisher. In the late 1980s, he went to Japan to promote French comics, but instead, he discovered Japanese manga. He brought the manga Akira to France and published it in 1990. This was very important because it was the first big success for manga in France.
9. What was the first big manga success in France?
The first big manga success in France was Akira by Katsuhiro Otomo. It was published in 1990 and helped make manga popular in France.
10. What other famous manga did Glénat publish?
After Akira, Jacques Glénat also published Dragon Ball, which became very popular in France. This manga helped make manga culture grow even more.
📈 3. The Manga Boom (1990s–2000s)
11. What happened to manga in France during the 1990s?
There was a big boom of manga in France during the 1990s and 2000s. Many publishers started to bring manga to France, and many popular titles appeared, like Sailor Moon, Naruto, One Piece, and Bleach. Manga became very popular with readers of all ages.
12. Can you name some popular manga titles from that time?
Some popular manga titles were Ken (Ken le Survivant), Dragon Ball, City Hunter, Sailor Moon, Ranma ½, and Gunnm. These mangas became very famous in France.
13. What was special about how manga was printed in France?

Manga in France was printed in the original right-to-left format. This means readers could read the books just like in Japan. This helped keep the authentic Japanese style and made manga more popular.

🎌 4. Cultural Recognition

"""

tts = gTTS(text, lang='en')
tts.save("manga_intro_english.mp3")

print("File saved as manga_intro_english.mp3")
