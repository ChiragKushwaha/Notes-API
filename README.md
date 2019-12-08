<h1>GET REQUEST</h1>


<h2>url :</h2><h3>http://127.0.0.1:8000/<h3>                <mark><h4>sends the url where notes are stored</h4></mark>
<pre>{
    "note": "http://127.0.0.1:8000/note/"
}</pre>




<h1>structure of note</h1>
<pre>[
    {
        "id": ,
        "title": ,
        "description": ,
        "creation_date": ,
        "updated_on_date": ,
        "url": 
    }
}</pre>




<h2>url :</h2><h3>http://127.0.0.1:8000/note</h3>      <mark><h4>sends all the notes created</h4></mark>
<pre>[
    {
        "id": 4,
        "title": "Ram",
        "description": "Ramayan book is famous",
        "creation_date": "2019-12-08T20:10:00.536289Z",
        "updated_on_date": "2019-12-08T20:10:00.536289Z",
        "url": "http://127.0.0.1:8000/note/4/"
    },
    {
        "id": 3,
        "title": "Physics",
        "description": "You can do anything if you the Science behind it.",
        "creation_date": "2019-12-08T19:58:27.965613Z",
        "updated_on_date": "2019-12-08T19:58:27.965613Z",
        "url": "http://127.0.0.1:8000/note/3/"
    },
    {
        "id": 2,
        "title": "Biology",
        "description": "Nice Subjects .",
        "creation_date": "2019-12-08T19:57:59.168590Z",
        "updated_on_date": "2019-12-08T19:57:59.168590Z",
        "url": "http://127.0.0.1:8000/note/2/"
    },
    {
        "id": 1,
        "title": "maths",
        "description": "do homework of maths.",
        "creation_date": "2019-12-08T19:57:43.945218Z",
        "updated_on_date": "2019-12-08T19:57:43.945218Z",
        "url": "http://127.0.0.1:8000/note/1/"
    }
]</pre>






<h2>url :</h2><h3>http://127.0.0.1:8000/note/1</h3>        <mark><h4>Can retrieve a note with it's id number</h4></mark>
<pre>{
    "id": 1,
    "title": "maths",
    "description": "do homework of maths.",
    "creation_date": "2019-12-08T19:57:43.945218Z",
    "updated_on_date": "2019-12-08T19:57:43.945218Z",
    "url": "http://127.0.0.1:8000/note/1/"
}</pre>



<h1>POST REQUEST</h1>

<h2>url :</h2><h3>http://127.0.0.1:8000/note/</h3>          <mark><h4>Creation of new note</h4></mark>
<pre>{
    "title": [
        "This field is required."
    ],
    "description": [
        "This field is required."
    ]
}</pre>



<h1>PUT REQUEST</h1>
<h2>url :</h2><h3>http://127.0.0.1:8000/note/1/</h3>          <mark><h4>POST UPDATION Using it's id number</h4></mark>
<pre>{
    "title": [
        "This field is required."
    ],
    "description": [
        "This field is required."
    ]
}</pre>

<h1>DELETE REQUEST</h1>
<h2>url :</h2><h3>http://127.0.0.1:8000/note/3/</h3>         <mark><h4>Dekete by id number</h4></mark>


