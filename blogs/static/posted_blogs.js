function increment_likes()
{
var likes = document.getElementById("demo").innerHTML;
likes = parseInt(likes) + 1;
likes = likes.toString();
document.getElementById("demo").innerHTML = likes;
try
{
var data = new FormData();
var xhr = new XMLHttpRequest();
var csrftoken = Cookies.get('csrftoken');
data.append('likes', likes);
xhr.open('POST', '../likeblog/', true);
xhr.setRequestHeader('X-CSRFToken', csrftoken);
xhr.send(data);
}
catch(err)
{
alert(err.message);
}
}

function increment_dislikes()
{
var dislikes = document.getElementById("demo1").innerHTML;
dislikes = parseInt(dislikes) + 1;
dislikes = dislikes.toString();
document.getElementById("demo1").innerHTML = dislikes;
try
{
var count = new FormData();
var xhr = new XMLHttpRequest();
var csrftoken = Cookies.get('csrftoken');
count.append('dislikes', dislikes);
xhr.open('POST', '../dislikeblog/', true);
xhr.setRequestHeader('X-CSRFToken', csrftoken);
xhr.send(count);
}
catch(err)
{
alert(err.message);
}
}

function save_blog()
{
var blog_data = new FormData();
var xhr = new XMLHttpRequest();
var csrftoken = Cookies.get('csrftoken');
var fields = document.getElementsByTagName("META");
try
{
for (var i = 0; i < fields.length; i++)
{
 blog_data.append(fields[i].name,fields[i].content);
}
xhr.open('POST', '../saveblog/', true);
xhr.setRequestHeader('X-CSRFToken', csrftoken);
xhr.send(blog_data);
}
catch(err)
{
alert(err.message);
}
}


