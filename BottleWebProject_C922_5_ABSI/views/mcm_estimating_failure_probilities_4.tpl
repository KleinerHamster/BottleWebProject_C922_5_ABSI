% rebase('layout.tpl', title='Home Page', year=year)

    <p></p>
    <headerHP2>Simulation modeling. Queuing systems</headerHP2>
    <headerHP2>Monte Carlo method for finding the mathematical expectation</headerHP2>

<h3> Input </h3>
<form action="/mcm_estimating_failure_probilities_4" method="post">

        <!-- добавл€ем текстовое поле дл€ почты, использу€ паттерн-->
        <p><input type="number" step="0.01" size="50" id="t1" name="t1" placeholder="t1" required oninvalid="this.setCustomValidity('Enter first parameters!')" 
        oninput="this.setCustomValidity('')"></p>

        <!-- добавл€ем текстовое поле дл€ почты, использу€ паттерн-->
        <p><input type="number" step="0.01" size="50" id="t2" name="t2" placeholder="t2" required oninvalid="this.setCustomValidity('Enter second parameters!')" 
        oninput="this.setCustomValidity('')"></p>

        <!-- добавл€ем текстовое поле дл€ почты, использу€ паттерн-->
        <p><input type="number" step="0.01" size="50" id="a" name="a" placeholder="a" required oninvalid="this.setCustomValidity('Enter third parameters!')" 
        oninput="this.setCustomValidity('')"></p>

        <!-- добавл€ем текстовое поле дл€ почты, использу€ паттерн-->
        <p><input type="number" size="50" id="n" name="n" placeholder="n" required oninvalid="this.setCustomValidity('Enter fourth parameters!')" 
        oninput="this.setCustomValidity('')"></p>

        <!-- кнопка дл€ отправки-->
        <p><input type="submit"  class="btn btn-default" value="Send"></p>

</form>

<hr class="about">

<pHP1>Example</pHP1>
<p></p>

<pAbout>Task conditions.
<br>
A four-channel queuing system with failures receives a Poisson flow of applications. 
The time between the receipt of two consecutive applications is distributed according to 
the exponential law f(TAU)=5e^(-5TAU). The service duration of each application is 0.5 minutes. 
Find by the Monte Carlo method the mathematical expectation a of the number of applications 
served during the time T = 4 min.
<br><br>Solving.
<br>Let T1=0 be the moment of receipt of the first application. The application will be sent to 
the first channel and will be served by it. The time of the end of the service of the first application 
T1+0.5=0+0.5=0.5. In the counter of serviced applications, we write one.
<br>The moments of receipt of subsequent applications will be found by the formula 
<br>Ti=Ti-1+TAUi,
<br>where TAUi is the length of time between two consecutive applications with numbers i-1 and i.
<br>Possible TAUi = -(1/LAMBDA)ln TAUi.
<br>Given that, by the condition, LAMBDA=5, we get  = -0.2 ln ri.
Random numbers ri are generated using a random number generator. Let the time between the receipt of the 
first and second applications be a random number equal to r1 = 0.10.
<br>Then TAU2=-0.2*ln(0.10)=0.460. The first application was received at the moment T1=0. Therefore, 
the second application was received at the moment T2=T1+0.460=0+0.460=0.460. At this moment, 
the first channel is still busy servicing the first application, so the second application will 
arrive in the second and will be serviced by it. 
<br>The end of the service of the second application is T2+0.5=0.460+0.5=0.960. We add one to the 
counter of served requests. 
<br>According to the next random number r2=0.09, we will play the time TAU3 between the receipt 
of the second and third applications:
<br>TAU3=-0.2*ln(0.09)=0.2*2.41=0.482. 
<br>The second application was received at the time T2= 0.460. 
Therefore, the third application was received at the moment T3=T2+0.482=0.460+0.482=0.942. 
At this moment, the first channel is already free, and the third application will be received
in the first channel. The end of the service of the third application is T3+0.5=0.942+0.5=1.442. 
We add one to the counter of served requests. Further calculation is performed similarly (Table 2), 
moreover, if at the time of receipt of the application all channels are busy (the time of receipt of 
the application is less than each of the moments of the end of service), then one is added to the failure counter.
<br>Note that the service of the 20th application will end at the moment 4.148>4, so this application is rejected.
<br>The test is terminated ("stop" is recorded in the table) if the time of receipt of the application is T>4.



</pAbout>

<iframe width="1050" height="760" frameborder="0" scrolling="no" src="https://onedrive.live.com/embed?resid=64BE450E1A82AA1A%217489&authkey=%21AOjobiUA_xsLwPU&em=2&wdAllowInteractivity=False&wdHideGridlines=True&wdHideHeaders=True&wdDownloadButton=True&wdInConfigurator=True&wdInConfigurator=True&edesNext=false&ejss=false"></iframe>

<pAbout>
<br>From the table we find that in 4 minutes a total of 20 applications were received; x1 = 17 were served. 
<br>Let's perform five more tests in the same way, we get:
<br>x2=15, x3=14, x4=17, x5 =13, x6=15.
<br>As an estimate of the desired mathematical expectation a Ц the number of applications served, we will take a sample average:
<br>a=(2*17+13+14+2*15)/6=15.2
<br><br>result: a=15.2
</pAbout>