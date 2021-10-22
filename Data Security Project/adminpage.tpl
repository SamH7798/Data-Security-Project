<html>
<header>
  <title>COVID Web Collector</title>
  <meta charset="utf-8">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</header>

<style>
table, th, td {
    border: 1px solid black;
}
</style>
</head>

<body>
<div class="container">
  <h2>Grant Access</h2>
  <form action="/grant_request" method="post">
    <div class="form-group">
      <label for="Email">Enter Email</label>
      <input type="text" class="form-control" id="email" name="email" placeholder="Enter email to grant access"/>
    </div>

<table>
% i = 0

%while i < len(names):
    
    <tr><td>{{names[i]}}</td> <td>{{emails[i]}}</td> </tr>
%    i = i + 1
% end

</table>



    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
</div>


</body>
</html>
