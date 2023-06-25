import tkinter as tk
import os
from tkinter import filedialog
from SpectralData import SpectroscopicData, SpectrumDataPoint

class SpectroscopicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Spectroscopic Analysis")

        # Dropdown menus
        self.user_directory = r"C:\Users\youcheng.wang\Desktop\Analysis"  # Set the desired user directory
        self.file_menu = tk.OptionMenu(self.root, tk.StringVar(), *self.get_file_list(self.user_directory))
        self.file_menu.pack()

        # Buttons
        self.select_button = tk.Button(self.root, text="Select Files", command=self.select_files)
        self.select_button.pack()

        self.calculate_button = tk.Button(self.root, text="Calculate Difference Spectrum", command=self.calculate_spectrum)
        self.calculate_button.pack()

    def get_file_list(self, user_directory):
        # Return a list of ".dat" file names in the specified user directory
        file_list = []
        for filename in os.listdir(user_directory):
            if filename.endswith(".dat"):
                file_list.append(filename)
        return file_list

    def select_files(self):
        # Open file dialog to select two files
        file1 = filedialog.askopenfilename(title="Select File 1", filetypes=(("Text Files", "*.dat"),))
        file2 = filedialog.askopenfilename(title="Select File 2", filetypes=(("Text Files", "*.dat"),))

        # Calculate and generate difference spectrum
        self.calculate_difference_spectrum(file1, file2)

    def calculate_difference_spectrum(self, file1, file2):
        # Create instances of SpectroscopicData for the selected files
        data1 = SpectroscopicData(file1)
        data2 = SpectroscopicData(file2)

        spectrum1 = data1.read_data(file1)
        spectrum2 = data2.read_data(file2)

        # Calculate difference spectrum
        # Modify this part according to your specific logic for generating the difference spectrum
        difference_spectrum = []
        for i in range(len(spectrum1)):
            channel_name = spectrum1[i].channel_name
            wavelength = spectrum1[i].wavelength
            reading1 = spectrum1[i].reading
            reading2 = spectrum2[i].reading
            difference = reading2 - reading1
            data_point = SpectrumDataPoint(channel_name, wavelength, difference)
            difference_spectrum.append(data_point)

        # Save difference spectrum to a new file
        # Modify this part to save the spectrum with a new name as per user's choice
        output_file = os.path.join(self.user_directory, "difference_spectrum.txt")
        with open(output_file, "w") as f:
        # Write the column headers
            f.write("Channel Name\tWavelength\tReading Difference\n")
            for data_point in difference_spectrum:
                line = f"{data_point.channel_name}\t{data_point.wavelength}\t{data_point.reading}\n"
                f.write(line)

        print("Difference spectrum saved to:", output_file)

    def calculate_spectrum(self):
        # Placeholder method for calculating the difference spectrum
        print("Calculating difference spectrum...")


if __name__ == "__main__":
    root = tk.Tk()
    app = SpectroscopicApp(root)
    root.mainloop()
