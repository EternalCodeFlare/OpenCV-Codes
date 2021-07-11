# Function to load an image, Flip & Grayscale conversion of the image using Numpy
# Show the image again

selected_image = 'Beach' 
flip_image_horizontally = True 
convert_image_to_grayscale = False 

image_path = #Image_path
image_np = load_image_into_numpy_array(image_path)

# Flip horizontally
if(flip_image_horizontally):
  image_np[0] = np.fliplr(image_np[0]).copy()

# Convert image to grayscale
if(convert_image_to_grayscale):
  image_np[0] = np.tile(
    np.mean(image_np[0], 2, keepdims=True), (1, 1, 3)).astype(np.uint8)

plt.figure(figsize=(24,32))
plt.imshow(image_np[0])
plt.show()