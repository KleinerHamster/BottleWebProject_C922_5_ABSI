<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - Simulation Modeling</title>
    <link rel="stylesheet" type="text/css" href="/static/content/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/site.css" />
    <script src="/static/scripts/modernizr-2.6.2.js"></script>

</head>

<body>
    <nav class="navbar navbar-custom navbar-fixed-top">
      <div class="container-fluid">
        <div class="navbar-header">
          <a class="navbar-brand" href="/">
          <!-- ����������� ���� ����� -->
           <img src="static\images\home\logo.png" alt="logo" style="width:80px;height:28px;">
          </a>
        </div>
        <!-- ����������� ������-������ ��������� ���� -->
        <ul class="nav navbar-nav">
            <li><a class="navbar-brand" href="/home">Simulation modeling</a></li><!-- ������-������ �� ������� �������� -->
            <li><a class="navbar-brand" href="/mcm_system_reliability_3_2" title="System realiability 3 and 2 thread">MCM 3 and 2 tread</a></li><!-- ������-������ �� 3 � 2 ��������� ������� ��� -->
            
            <li><a class="navbar-brand" href="/mcm_estimating_failure_probilities_3" title="Estimating failure probilities 3 tread">MCM 3 tread</a></li><!-- ������-������ �� 3 ��������� ��� -->
            <li><a class="navbar-brand" href="/mcm_estimating_failure_probilities_4" title="Estimating failure probilities 4 tread">MCM 4 tread</a></li><!-- ������-������ �� 4 ��������� ���� -->

            <li><a class="navbar-brand" href="/mcm_system_reliability_2_3" title="System realiability 2 and 3 thread">MCM 2 and 3 tread</a></li><!-- ������-������ �� 2 � 3 ��������� ������� ��� -->
            <li><a class="navbar-brand" href="/about">About us</a></li><!-- ������-������ �� ������ �� ������� -->
            
        </ul>
      </div>
    </nav>

    <!-- ����������� ����� �������� -->
    <div class="container body-content">
        {{!base}}
        <footer>
            <pEnd>&copy; {{ year }} - KVAS Corporation</pEnd>
        </footer>
    </div>
    <script src="/static/scripts/jquery-1.10.2.js"></script>
    <script src="/static/scripts/bootstrap.js"></script>
    <script src="/static/scripts/respond.js"></script>

</body>
</html>
