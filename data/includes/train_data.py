import numpy as np
import random
from PIL import Image, ImageOps
from os import listdir

class Data:
    """ Get train data """
    photo_height = 96
    photo_width = 96
    bad = 'photos/training/bad'
    good = 'photos/training/good'
    test_path = 'photos/test'

    def __init__(self):
        pass
    
    def get_file_data(self, file_path, x_centering = 0.5, y_centering = 0.5):
        """
        Get data for an photo file.

        Attributes
        ----------
        file_path : string
            Path of photo file.
        x_centering : float
            The x centering
        y_centering : float
            The y centering

        Returns
        -------
        numpy.array
            Array with photo values.
        """
        return np.asarray(ImageOps.fit(Image.open(file_path),
            (self.photo_width, self.photo_height), Image.ANTIALIAS, 0, (x_centering, y_centering)))/255.0

    def verify_photo(self, file_path):
        """
        Verify file is image.

        Attributes
        ----------
        file_path : string
            Path of photo file.

        Returns
        -------
        boolean
            True if it is file.
        """
        try:
            photo = Image.open(file_path)
            photo.verify()
            return True
        except Exception:
            return False
    
    def get_photos_from_path(self, folder_path):
        """
        Get all photos from path.

        Attributes
        ----------
        folder_path : string
            Path of photo folder.

        Returns
        -------
        numpy.array
            Array of arrays of photo values.
        """
        photos = []
        for filename in listdir(folder_path):
            try:
                if (self.verify_photo(folder_path + '/' + filename)):
                    for i in range(5):
                        # Get multiple cuts of the same photo.
                        x_centering = round(random.uniform(0, 1), 1)
                        y_centering = round(random.uniform(0, 1), 1)
                        photos.append([self.get_file_data(folder_path + '/' + filename, x_centering, y_centering), filename])
            except IOError:
                # print('Found one non photo file.')
                pass
        return photos

    def get_training_photos(self):
        """
        Get all training photos.

        Returns
        -------
        array
            Array of training photos with labels.
        """
        data = []
        
        # Get good photos.
        for item in self.get_photos_from_path(self.good):
            data.append([item[0], [1, 0]])

        # Get bad photos.
        for item in self.get_photos_from_path(self.bad):
            data.append([item[0], [0, 1]])
        
        random.shuffle(data)

        return np.asarray([item[0] for item in data]), np.asarray([item[1] for item in data])

    def get_test_photos(self):
        """
        Get test photos.

        Returns
        -------
        array
            Array of test photos.
        """
        return self.get_photos_from_path(self.test_path)