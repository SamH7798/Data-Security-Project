<html>
<header>
  <title>COVID Web Collector</title>
  <meta charset="utf-8">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</header>

<body>
<div class="container">
  <h2>Request Access</h2>
  <form action="/request" method="post">
    <div class="form-group">
      <label for="code">Name:</label>
      <input type="text" class="form-control" id="code" name="code" placeholder="Enter your name"/>
    </div>
    <div class="form-group">
      <label for="email">Email:</label>
      <input type="text" class="form-control" id="email" name="email" placeholder="Enter email"/>    
    </div>


    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
<div>
<hr>
<a href="/accesspage">Once you have been given a code click here</a> 


</div>
<hr/>

</body>
</html>