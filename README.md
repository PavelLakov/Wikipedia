# Encyclopedia Project

## Introduction

Diving into the digital age, the thirst for knowledge is more pervasive than ever. Inspired by the vast expanse of Wikipedia, the Encyclopedia Project aims to bring a slice of this infinite repository into a more intimate, user-driven space. Born from the idea that information should be accessible, editable, and organizable by anyone, our project is a testament to the collaborative spirit of the modern web

## What Sets Us Apart

Unlike Wikipedia, which uses a complex syntax called Wikitext for its entries, our Encyclopedia simplifies the creation and editing process by utilizing Markdown—a lightweight markup language with plain-text formatting syntax. This choice ensures that anyone, regardless of their technical background, can contribute to and expand our knowledge base with ease.

## Core Features

### Dynamic Entry Pages

Each topic or concept is housed within its own dedicated page, allowing users to dive deep into subjects without the distraction of unrelated information.

### Effortless Navigation

Our Index Page acts as the portal to discovery, listing every entry in the encyclopedia in one accessible location.

### Powerful Search Functionality

The quest for knowledge is made seamless with our intuitive search feature, which adeptly finds entries that contain your query, ensuring that information is always at your fingertips.

### User-Centric Creation

The "Create New Page" feature invites users to be the architects of knowledge, encouraging the addition of new entries through an easy-to-use Markdown editor.

### Simplified Editing

Every entry is a living document, open to refinement and expansion through our straightforward editing interface, pre-populated with the existing Markdown content.

### Surprise Me

The "Random Page" feature caters to the curious at heart, offering serendipitous exploration of topics at the click of a button.

### From Markdown to Majestic HTML

 Utilizing the python-markdown2 package, we transform Markdown into beautifully rendered HTML, ensuring that entries are not only informative but also pleasing to the ey

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed:

- Python (3.x recommended)
- pip (Python package installer)
- Django
- python-markdown2 (for Markdown to HTML conversion)
  -pip install django markdown2

### Installation

1. **Clone the Repository
   to your local machine**

2. **Navigate to the Project Directory**

- cd encyclopedia

1. **Create and Activate a Virtual Environment**
Before installing the required packages, it's a good practice to create a virtual environment. This isolates your project dependencies from other Python projects on your system.

*To create a virtual environment*, run:

- python -m venv env
  
*To activate the virtual environment on Windows, run:*

- .\env\Scripts\activate
  
*On macOS and Linux, use:*

- source env/bin/activate

3. **Install the Required Python Packages
Install Django and the python-markdown2 library, along with any other necessary libraries using pip**

- pip install django markdown2

4. **Run the Django Development Server**

*Launch the development server to start the application:*

- python manage.py runserver

5. **View the Encyclopedia**

  *Open a web browser and navigate to <http://127.0.0.1:8000/> to see the encyclopedia in action.*

## License

Copyright (c) [2024] [Pavel Lakov]

The permission granted herein is limited exclusively to personal and non-commercial use of this software and associated documentation files (the "Software"). Any use of the Software beyond personal and non-commercial purposes is strictly prohibited and includes, but is not limited to, distribution, sublicensing, and sale of the Software or its copies.

All other rights are reserved by the copyright holder.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
