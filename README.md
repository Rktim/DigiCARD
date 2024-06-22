# DigiCARD


This project is a simple Streamlit-based web application that allows users to generate a personalized digital card. The digital card includes user information, a profile picture, and a QR code that encapsulates the user's biodata. The generated card can be viewed within the app and downloaded for personal use.

## Features

- **User Information Input**: Enter your name, age, gender, occupation, email, phone number, address, LinkedIn ID, GitHub Repo, and optionally, your Instagram and Facebook IDs.
- **Image Upload**: Upload a profile picture in PNG, JPG, or JPEG format.
- **QR Code Generation**: Automatically generates a QR code with your biodata.
- **Digital Card Creation**: Combines user data, profile picture, and QR code into a single digital card.
- **Card Preview and Download**: View the generated digital card within the app and download it for offline use.


## Usage

1. Open the application in your web browser. You will see a form with fields to enter your personal information.

2. Fill in the required fields:
   - **Name**
   - **Age**
   - **Gender**
   - **Occupation**
   - **Email**
   - **Phone**
   - **Address**
   - **LinkedIn ID**
   - **GitHub Repo**

3. Optionally, fill in the additional fields:
   - **Instagram ID**
   - **Facebook ID**

4. Upload your profile picture by clicking on "Upload your image" and selecting an image file from your device.

5. Click the "Generate Digital Card" button to create your digital card. If any required fields are missing or no image is uploaded, you will see an error message prompting you to complete all necessary information.

6. Once the digital card is generated, it will be displayed within the application. You can download the card by clicking the "Download Digital Card" button.

## Code Overview

### `create_digital_card` Function

This function creates a digital card using the provided biodata and image.

- **Parameters**:
  - `biodata`: A dictionary containing user information.
  - `image_path`: The path to the uploaded profile image.

- **Steps**:
  1. Create a new image with a specified background color.
  2. Load and resize the profile picture.
  3. Draw the user information on the card.
  4. Generate and resize a QR code with the biodata.
  5. Paste the profile picture and QR code onto the card.
  6. Save the final card as an image file and return the filename.

### Streamlit UI

- The Streamlit UI collects user input through various fields and handles the image upload.
- It validates that all required fields are filled and an image is uploaded before allowing card generation.
- Once the card is generated, it is displayed in the app, and a download button is provided for the user to save the card.

## Dependencies

- **Streamlit**: For creating the web application.
- **Pillow**: For image processing.
- **qrcode**: For generating QR codes.

## Acknowledgements

Special thanks to the creators and maintainers of the libraries used in this project.

## Contributing

Contributions are welcome! If you have any ideas or improvements, feel free to open an issue or submit a pull request.

## Contact

For any questions or feedback, please reach out to raktmxx@gmail.com .
