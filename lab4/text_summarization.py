# %% Imports and defining text data
from numpy.core.fromnumeric import argmax
from summa.summarizer import summarize
from summa.keywords import keywords

pizza_text = """
Foods similar to pizza have been made since the Neolithic Age.Records of people adding other ingredients to bread to make it more flavorful can be found throughout ancient history. In the 6th century BC, the Persian soldiers of Achaemenid Empire during the rule King Darius I baked flatbreads with cheese and dates on top of their battle shields and the ancient Greeks supplemented their bread with oils, herbs, and cheese. An early reference to a pizza-like food occurs in the Aeneid, when Celaeno, queen of the Harpies, foretells that the Trojans would not find peace until they are forced by hunger to eat their tables (Book III). In Book VII, Aeneas and his men are served a meal that includes round cakes (like pita bread) topped with cooked vegetables. When they eat the bread, they realize that these are the "tables" prophesied by Celaeno.

Modern pizza evolved from similar flatbread dishes in Naples, Italy, in the 18th or early 19th century. Prior to that time, flatbread was often topped with ingredients such as garlic, salt, lard, and cheese. It is uncertain when tomatoes were first added and there are many conflicting claims. Until about 1830, pizza was sold from open-air stands and out of pizza bakeries.
"""

review_text = """
The Shawshank Redemption is written and directed by Frank Darabont. It is an adaptation of the Stephen King novella Rita Hayworth and Shawshank Redemption. Starring Tim Robbins and Morgan Freeman, the film portrays the story of Andy Dufresne (Robbins), a banker who is sentenced to two life sentences at Shawshank State Prison for apparently murdering his wife and her lover. Andy finds it tough going but finds solace in the friendship he forms with fellow inmate Ellis "Red" Redding (Freeman). While things start to pick up when the warden finds Andy a prison job more befitting his talents as a banker. However, the arrival of another inmate is going to vastly change things for all of them.

There was no fanfare or bunting put out for the release of the film back in 94, with a title that didn't give much inkling to anyone about what it was about, and with Columbia Pictures unsure how to market it, Shawshank Redemption barely registered at the box office. However, come Academy Award time the film received several nominations, and although it won none, it stirred up interest in the film for its home entertainment release. The rest, as they say, is history. For the film finally found an audience that saw the film propelled to almost mythical proportions as an endearing modern day classic. Something that has delighted its fans, whilst simultaneously baffling its detractors. One thing is for sure, though, is that which ever side of the Shawshank fence you sit on, the film continues to gather new fans and simply will never go away or loose that mythical status.

It's possibly the simplicity of it all that sends some haters of the film into cinematic spasms. The implausible plot and an apparent sentimental edge that makes a nonsense of prison life, are but two chief complaints from those that dislike the film with a passion. Yet when characters are this richly drawn, and so movingly performed, it strikes me as churlish to do down a human drama that's dealing in hope, friendship and faith. The sentimental aspect is indeed there, but that acts as a counterpoint to the suffering, degradation and shattering of the soul involving our protagonist. Cosy prison life you say? No chance. The need for human connection is never more needed than during incarceration, surely? And given the quite terrific performances of Robbins (never better) & Freeman (sublimely making it easy), it's the easiest thing in the world to warm to Andy and Red.

Those in support aren't faring too bad either. Bob Gunton is coiled spring smarm as Warden Norton, James Whitmore is heart achingly great as the "Birdman Of Shawshank," Clancy Brown is menacing as antagonist Capt. Byron Hadley, William Sadler amusing as Heywood & Mark Rolston is impressively vile as Bogs Diamond. Then there's Roger Deakins' lush cinematography as the camera gracefully glides in and out of the prison offering almost ethereal hope to our characters (yes, they are ours). The music pings in conjunction with the emotional flow of the movie too. Thomas Newman's score is mostly piano based, dovetailing neatly with Andy's state of mind, while the excellently selected soundtrack ranges from the likes of Hank Williams to the gorgeous Le Nozze di Figaro by Mozart.

If you love Shawshank then it's a love that lasts a lifetime. Every viewing brings the same array of emotions - anger - revilement - happiness - sadness - inspiration and a warmth that can reduce the most hardened into misty eyed wonderment. Above all else, though, Shawshank offers hope - not just for characters in a movie - but for a better life and a better world for all of us. 10/10
"""

article_text = """
For thousands of years, the dainty Fritillaria delavayi has grown slowly on the rocky slopes of the Hengduan mountains in China, producing a bright green flower after its fifth year.

But the conspicuous small plant has one deadly enemy: people, who harvest the flower for traditional Chinese medicine.

As commercial harvesting has intensified, Fritillaria delavayi has vanished – by rapidly evolving to produce grey and brown leaves and flowers that cannot be so easily seen by pickers.

Scientists have discovered that the colour of the plant’s leaves has become more camouflaged – matching the background rocks on which they grow – in areas where there is more harvesting pressure from people.

“Like other camouflaged plants we have studied, we thought the evolution of camouflage of this fritillary had been driven by herbivores, but we didn’t find such animals,” said Dr Yang Niu, of the Kunming Institute of Botany, and co-author of the study in Current Biology. “Then we realised humans could be the reason.”

In the study by the Kunming Institute of Botany (Chinese Academy of Sciences) and the University of Exeter, researchers measured how closely plants from different populations matched their mountain environment and how easy they were to collect, and interviewed local people to estimate how much harvesting took place in each location.

In a computer experiment, people were found to take more time to discover the more-camouflaged plants, suggesting that humans are driving the rapid evolution of this species into new colour forms because better-camouflaged plants have a higher chance of survival.

Fritillaria delavayi is a perennial herb that grows leaves at a young age before producing a single flower after its fifth year every June. The bulb of the fritillary species has been used in traditional Chinese medicine for more than 2,000 years but high prices in recent years have led to increased harvesting.

“It’s remarkable to see how humans can have such a direct and dramatic impact on the colouration of wild organisms, not just on their survival but on their evolution itself,” said Prof Martin Stevens, of the Centre for Ecology and Conservation at the University of Exeter. “Many plants seem to use camouflage to hide from herbivores that may eat them – but here we see camouflage evolving in response to human collectors.

“It’s possible that humans have driven evolution of defensive strategies in other plant species, but surprisingly little research has examined this.”
"""

# %% Summarize and get top 5 keywords
print('Summary:\n%s' % summarize(article_text, ratio=0.1))
print('\nKeywords:\n%s' % keywords(article_text, words=4))
