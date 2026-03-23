# ==============================
# 📌 Project: LexiScrape
# 📌 Description:
# Web Scraping + NLP Text Analysis using NLTK
# ==============================

# Import required libraries
import urllib.request                      # For fetching data from URL
from bs4 import BeautifulSoup              # For parsing HTML content
import nltk                                # Natural Language Toolkit
from nltk.corpus import stopwords          # Stopwords for text cleaning
from nltk.probability import FreqDist      # Frequency distribution

# Download stopwords (only needed first time)
nltk.download('stopwords')

# ==============================
# 🌐 Step 1: Fetch Data from Website
# ==============================

url = 'https://en.wikipedia.org/wiki/AMAZON'  # URL to scrape
response = urllib.request.urlopen(url)     # Open URL
html = response.read()                    # Read HTML content

# ==============================
# 🧾 Step 2: Parse HTML Content
# ==============================

soup = BeautifulSoup(html, 'html5lib')    # Parse HTML using BeautifulSoup
text = soup.get_text(strip=True)          # Extract clean text

# ==============================
# 🔤 Step 3: Tokenization
# ==============================

tokens = text.split()                     # Split text into words (tokens)

# ==============================
# 🧹 Step 4: Remove Stopwords
# ==============================

stop_words = set(stopwords.words('english'))  # Load stopwords once

# Filter tokens (remove stopwords)
clean_tokens = [word for word in tokens if word.lower() not in stop_words]

# ==============================
# 📊 Step 5: Frequency Analysis
# ==============================

freq_dist = FreqDist(clean_tokens)        # Create frequency distribution

# ==============================
# 📈 Step 6: Visualization
# ==============================

# Plot top 50 most frequent words
freq_dist.plot(50, title="Top 50 Most Frequent Words")

# ==============================
# 📌 (Optional) Print Frequencies
# ==============================

# Uncomment below to print word counts
# for word, count in freq_dist.items():
#     print(f"{word}: {count}")