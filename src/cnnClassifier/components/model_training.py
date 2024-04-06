import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from pathlib import Path
from cnnClassifier.entity.config_entity import TrainingConfig


# Define the input shape
input_shape = (224, 224, 3)  # Example input shape for an image with height 224, width 224, and 3 channels (RGB)

# Define the input layer
input_layer = tf.keras.Input(shape=input_shape)

# Define the rest of your model layers
# For example:
x = tf.keras.layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu')(input_layer)


# Define the input layer
input_layer = tf.keras.Input(shape=(input_shape))

# Define the rest of your model layers
# For example:
x = tf.keras.layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu')(input_layer)
x = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))(x)
x = tf.keras.layers.Flatten()(x)
x = tf.keras.layers.Dense(128, activation='relu')(x)

# Now, define the output layer using the correct output from the previous layer
num_classes = 2  # Example number of classes
output_layer = tf.keras.layers.Dense(num_classes, activation='softmax')(x)

# Create the model
model = tf.keras.Model(inputs=input_layer, outputs=output_layer)



class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config
        self.steps_per_epoch = None  # Initialize steps_per_epoch attribute
        self.validation_steps = None

    def get_base_model(self):
        # Load the base model
        self.base_model = tf.keras.models.load_model(self.config.updated_base_model_path)

        # Adjust the output layer for your classification task
        num_classes = 2  # Example number of classes
        output_layer = tf.keras.layers.Dense(num_classes, activation='softmax')(self.base_model.output)
        self.model = tf.keras.Model(inputs=self.base_model.input, outputs=output_layer)

    def train_valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.20
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else:
            train_datagenerator = valid_datagenerator

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )

    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)



    
    def train(self):
        # Compile the model
        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        # Train the model
        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_data=self.valid_generator,
            validation_steps=self.validation_steps
        )

        # Save the trained model
        self.save_model(path=self.config.trained_model_path, model=self.model)