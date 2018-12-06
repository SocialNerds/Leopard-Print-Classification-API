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

1. Training photos,
- Convince your special someone to find and classify at least 400 photos of leopard print 
- Place the good leopard print photos in data/photos/training/good
- Place the bad leopard print photos in data/photos/training/bad

3. Train your model,
~~~~
docker exec -it ai python train.py 1
~~~~

4. To find out if a leopard print is to your's special someone liking, place it in,
~~~~
data/photos/test
~~~~

5. Run your model,
~~~~
docker exec -it ai python predict.py 1
~~~~

6. You should see, something like,
~~~~
Using TensorFlow backend.
                       Good Leopardism
Bad_Leopard_126.jpeg              17.2
Bad_Leopard_159.jpeg              57.2
Bad_Leopard_225.jpeg              96.8
Bad_Leopard_277.jpeg              12.0
Bad_Leopard_357.png                2.0
Bad_Leopard_366.png               93.6
Bad_Leopard_380.png               57.3
Good_Leopard_163.jpeg             41.8
Good_Leopard_198.jpeg             47.6
Good_Leopard_215.jpeg             31.8
Good_Leopard_240.png              87.5
Good_Leopard_253.png              18.4
Good_Leopard_5.jpeg               99.0
~~~~

`Now, you finally know!`

7. Shut down container(s),
~~~~
docker-compose down
~~~~

# By SocialNerds
* [SocialNerds.gr](https://www.socialnerds.gr/)
* [YouTube](https://www.youtube.com/SocialNerdsGR)
* [Facebook](https://www.facebook.com/SocialNerdsGR)
* [Twitter](https://twitter.com/socialnerdsgr)