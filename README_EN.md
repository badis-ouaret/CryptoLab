--

## README (English)

### 🛠️ How to run the application:

1. Open a terminal or command prompt (**cmd**) in the project folder.
2. Run the following command:

   ```bash
   python3 app.py
   ```

📌 **Note**: Make sure **CustomTkinter** is installed beforehand.

---

### 🛍️ Application overview:

#### 🔹 Main window:

* Select the **encryption method** on the left using the radio buttons.
* Choose the **action** (encrypt / decrypt) using the radio buttons at the top.
* Enter your text in the left text box.
* Click the **"Encrypt"** or **"Decrypt"** button depending on the selected action.
* A **default key** will be used if no manual key is defined (see below for key definitions).
* The **result** will appear in the right text box.

---

### 🔑 Key definition windows:

* **Caesar**: accepts only integers between **0 and 27**.
* **Vigenère**: accepts **words without spaces** or **special characters**.
* **Improved Caesar**:

  * Each box represents an uppercase letter.
  * **No letter should be repeated.**
* **Polybius / Playfair**:

  * Start by defining the **paired characters**, from left to right.
  * Then enter your key: **uppercase letters only**, **no duplicates**.
  * The **second letter of each paired character is forbidden** in the key.
  * Click **"Preview"** to see the matrix.
* **Hill**:

  * Define the **matrix size**.
  * Fill in the matrix using your key values.
  * ⚠️ The matrix must be **invertible modulo 26**.
* **Affine**:

  * Provide the **key** and the **offset**.
  * ⚠️ The key must be **invertible modulo 26**.
* **DES**:

  * Provide a **binary key** with length ≤ **64 bits**.
  * It will be **automatically padded with zeros on the left** if needed.

📌 **Notes**:

* The **"Clear"** button only empties the fields, **it does not reset the keys**.
* To reset a key: first click **"Clear"**, then **"Validate"**.
