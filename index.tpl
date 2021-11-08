<DOCTYPE = html>
<Style>
Details{
  padding:5px;
}

h1{
  text-align:center;
  background-color: rgba(135,206,235,.3);
    background-blend-mode: multiply;
    background-size: cover;
    padding-bottom: 30px;
}
a{
    display: inline-block;
    padding:.5em;
    font-size: 1.2em;
    color:white;
    text-decoration: none;
}
a:hover{
    background-color: rgba(255,255,255,.1);
    }
</Style>
<header>
  <title>COVID Web Collector</title>
  <meta charset="utf-8">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</header>
<body>

<h1>Covid Web Collector</h1>
<div class="container">
  <h2>Help Us Gather Stastical Information</h2>
  <form action="/index" method="post">
    <div class="form-group">
      <label for="fullname">Name:</label>
      <input type="text" class="form-control" id="fullname" name="fullname" placeholder="Enter Full Name"/>
    </div>

    <div class="form-group">
      <label for="age">Age:</label>
      <input type="text" class="form-control" id="age" name="age" placeholder="Enter Age"/>    
    </div>

    <div class="form-group">
      <label for="symthom1">Most Intense Sythom</label>
      <input type="text" class="form-control" id="symthom1" name="symthom1" placeholder="Enter Your Worst Covid Symthom"/>    
    </div>

    <div class="form-group">
      <label for="symthon2">Most Intense Sythom</label>
      <input type="text" class="form-control" id="symthom2" name="symthom2" placeholder="Enter Your Second Worst Covid Symthom"/>    
    </div>
    <hr>
    <Details>
    <summary>Common Sythoms of Covid-19</summary>
    <ul>
        <li>Fevers</li>
        <li>Coughing</li>
        <li>Fatigue</li>
        <li>Difficulty breathing</li>
        <li>Body aches</li>
        <li>Loss of taste or smell</li>
        <li>Congestion</li>
        <li>Nausea</li>
        <li>Diarrhea</li>

    </ul>
    </Details>
    <hr>
    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
<div>
<hr>
<a href="/login">If you have an account, you can log in.</a> <a href="/adminlogin">Admin Login</a>
</body>
</html>