<?php

    include 'config.php';

    if (isset($_POST['post_comment'])) {

      $name = $_POST['name'];
      $grading = $_POST['grading'];


      $sql = "INSERT INTO comments (comments, grading)
      VALUES ('$name', '$grading')";

      if ($conn->query($sql) === TRUE) {
         echo "";
      } else {
         echo "Error: " . $sql . "<br>" . $conn->error;
      }
   }
?>

<!DOCTYPE html>
<html lang="en">
   <head>
      <!-- basic -->
      <meta charset="utf-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <!-- mobile metas -->
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <meta name="viewport" content="initial-scale=1, maximum-scale=1">
      <!-- site metas -->
      <title>CKW</title>
      <meta name="keywords" content="">
      <meta name="description" content="">
      <meta name="author" content="">
      <!-- bootstrap css -->
      <link rel="stylesheet" href="css/bootstrap.min.css">
      <!-- style css -->
      <link rel="stylesheet" href="css/style.css">
      <!-- Responsive-->
      <link rel="stylesheet" href="css/responsive.css">
      <!-- fevicon -->
      <link rel="icon" href="images/fevicon.png" type="image/gif" />
      <!-- Scrollbar Custom CSS -->
      <link rel="stylesheet" href="css/jquery.mCustomScrollbar.min.css">
      <!-- Tweaks for older IEs-->
      <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css">
      <!-- owl stylesheets --> 
      <link rel="stylesheet" href="css/owl.carousel.min.css">
      <link rel="stylesheet" href="css/owl.theme.default.min.css">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/fancybox/2.1.5/jquery.fancybox.min.css" media="screen">
   </head>
   <body>
      <!-- header section start -->
      <div class="header_section">
         <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container">
               <a class="logo" href="index.html"><img src="images/logo.png"></a>
               <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
               <span class="navbar-toggler-icon"></span>
               </button>
               <div class="collapse navbar-collapse" id="navbarSupportedContent">
                  <ul class="navbar-nav mr-auto">
                     <li class="nav-item">
                        <a class="nav-link" href="index.html">HOME</a>
                     </li>
                     <li class="nav-item">
                        <a class="nav-link" href="about.html">ABOUT</a>
                     </li>
                     <li class="nav-item">
                        <a class="nav-link" href="design.html">SHOP</a>
                     </li>
                     <li class="nav-item">
                        <a class="nav-link" href="contact.html">CONTACT US</a>
                     </li>
                  </ul>
                  <form class="form-inline my-2 my-lg-0">
                     <div class="search_icon">
                        <ul>
                           <li><a href="#"><img src="images/search-icon.png"></a></li>
                           <li><a href="login.html"><img src="images/user-icon.png"></a></li>
                        </ul>
                     </div>
                  </form>
               </div>
         </nav>
         </div>
      </div>
      <!-- header section end -->
      <!-- banner section start -->

      <!-- Main Body -->
      <section>
         <div class="container">
               <div class="row">
                  <div class="col-sm-5 col-md-6 col-12 pb-4">
                     <h1>Comments</h1>
                        <?php
                           $sql = "SELECT * FROM demo";
                           $result = $conn->query($sql);
                     
                           if ($result->num_rows > 0) {
                              // output data of each row
                              while($row = $result->fetch_assoc()) {
                        
                        ?>
                     <div class="comment mt-4 text-justify float-left">
                           <img src="https://i.imgur.com/CFpa3nK.jpg" alt="" class="rounded-circle" width="40" height="40">
                           <h4><?php echo $row['name']; ?></h4>
                           <br>
                           <p><?php echo $row['message']; ?></p>
                           <?php } } ?>
                     </div>
                  </div>
                  <div class="col-lg-4 col-md-5 col-sm-4 offset-md-1 offset-sm-1 col-12 mt-4">
                     <form id="algin-form">
                           <div class="form-group">
                              <h4>Leave a comment</h4>
                              <label for="message">Message</label>
                              <textarea name="msg" id=""msg cols="30" rows="5" class="form-control" style="background-color: rgb(255, 255, 255);"></textarea>
                           </div>
                           <div class="form-group">
                              <label for="name">Name</label>
                              <input type="text" name="name" id="fullname" class="form-control">
                           </div>
                           <div class="form-group">
                              <label for="email">Grading</label>
                              <input type="text" name="grading" id="grading" class="form-control">
                           </div>
                           <div class="form-group">
                              <button type="button" id="post" class="btn" name="post_comment">Post Comment</button>
                           </div>
                     </form>
                  </div>
               </div>
         </div>
      </section>
      <!-- Banner section end -->
      <!-- footer section start -->
      <div class="footer_section">
         <div class="container">
            <div class="footer_location_text">
               <ul>
                  <li><img src="images/map-icon.png"><span class="padding_left_10"><a href="#">Porsön, Luleå City</a></span></li>
                  <li><img src="images/call-icon.png"><span class="padding_left_10"><a href="#">Call : +46920 50 000</a></span></li>
                  <li><img src="images/mail-icon.png"><span class="padding_left_10"><a href="#">ckwfurniture@gmail.com</a></span></li>
               </ul>
            </div>
            <div class="row">
               <div class="col-lg-3 col-sm-6">
                  <h2 class="useful_text">Navigate </h2>
                  <div class="footer_menu">
                     <ul>
                        <li><a href="index.html">HOME</a></li>
                        <li><a href="about.html">ABOUT</a></li>
                        <li><a href="design.html">SHOP</a></li>
                        <li><a href="contact.html">CONTACT US</a></li>
                     </ul>
                  </div>
               </div>
               <div class="col-lg-3 col-sm-6">
                  <h2 class="useful_text">Work with us</h2>
                  <p class="lorem_text">We are always looking for new co-workers. Don't hesitate! </p>
               </div>
               <div class="col-lg-3 col-sm-6">
                  <h2 class="useful_text">Social Media</h2>
                  <div id="social">
                     <a class="facebookBtn smGlobalBtn active" href="#" ></a>
                     <a class="twitterBtn smGlobalBtn" href="#" ></a>
                     <a class="googleplusBtn smGlobalBtn" href="#" ></a>
                     <a class="linkedinBtn smGlobalBtn" href="#" ></a>
                  </div>
               </div>
               <div class="col-sm-6 col-lg-3">
                  <h1 class="useful_text">Our Repair center</h1>
                  <p class="footer_text">Our own repair center in Luleå gives us the possibility to provide costumers with cheap reapair service </p>
               </div>
            </div>
         </div>
      </div>
      <!-- footer section end -->
      <!-- copyright section start -->
      <div class="copyright_section">
         <div class="container">
            <p class="copyright_text">2023 All Rights Reserved. Design by <a href="https://www.ltu.se">CKW - group 21</a></p>
         </div>
      </div>
      <!-- copyright section end -->
      <!-- Javascript files-->
      <script src="js/jquery.min.js"></script>
      <script src="js/popper.min.js"></script>
      <script src="js/bootstrap.bundle.min.js"></script>
      <script src="js/jquery-3.0.0.min.js"></script>
      <script src="js/plugin.js"></script>
      <!-- sidebar -->
      <script src="js/jquery.mCustomScrollbar.concat.min.js"></script>
      <script src="js/custom.js"></script>
      <!-- javascript --> 
      <script src="js/owl.carousel.js"></script>
      <script src="https:cdnjs.cloudflare.com/ajax/libs/fancybox/2.1.5/jquery.fancybox.min.js"></script>
   </body>
</html>