# Leopard Print Classification API

Train a model to understand if a leopard print is good or bad. Occasionally you want to present
a gift, like a dress with leopard print, to your special someone and you just don't know if it is good or bad.
Your problems are over!

# Check the full explanation video (GR)
`(Pending)`
<!---
[![Αποκρυπτογράφηση Γυναικείου Μυαλού με AI, TensorFlow & Keras](https://img.youtube.com/vi/mKeI0Je9cKs/0.jpg)](https://www.youtube.com/watch?v=mKeI0Je9cKs)
-->

# Installation
Requirements
- You need to have [Docker](https://docs.docker.com/engine/installation/) installed

# Run

1. Run in root folder,
~~~~
cp .env.example .env
docker-compose build && docker-compose up -d
~~~~

`You could use the pretrained model. In that case, go to step 4.`

2. Training photos,
- Convince your special someone to find and classify at least 400 photos of leopard print 
- Place the good leopard print photos in data/photos/training/good
- Place the bad leopard print photos in data/photos/training/bad
- For better results, crop only the part that leopard print is visible

3. Train your model,
~~~~
docker exec -it ai python train.py 1
~~~~

4. To find out if a leopard print is to your's special someone liking, place it in,
~~~~
data/photos/test
~~~~

5. For better results, crop only the part that leopard print is visible

6. Run your model,
~~~~
docker exec -it ai python predict.py 1
~~~~

7. You should see, something like,
~~~~
Percentage (%) of Good Leopardism,

Bad_Leopard_105.jpeg   10.1
Bad_Leopard_132.jpeg    9.9
Bad_Leopard_165.jpeg   26.5
Bad_Leopard_172.jpeg    7.9
Bad_Leopard_3.jpeg     39.6
Bad_Leopard_375.png    69.2
Bad_Leopard_380.png     3.2
Bad_Leopard_385.png    61.7
Bad_Leopard_39.jpeg    42.7
Good_Leopard_1.jpeg    84.4
Good_Leopard_111.jpeg  75.8
Good_Leopard_12.jpeg   97.1
Good_Leopard_146.jpeg   1.0
Good_Leopard_171.jpeg  76.5
Good_Leopard_202.jpeg  61.9
Good_Leopard_232.png   70.9
Good_Leopard_25.jpeg    6.8
Good_Leopard_253.png   78.7
~~~~

`Now, you finally know!`

8. Shut down container(s),
~~~~
docker-compose down
~~~~

# By SocialNerds
* [SocialNerds.gr](https://www.socialnerds.gr/)
* [YouTube](https://www.youtube.com/SocialNerdsGR)
* [Facebook](https://www.facebook.com/SocialNerdsGR)
* [Twitter](https://twitter.com/socialnerdsgr)