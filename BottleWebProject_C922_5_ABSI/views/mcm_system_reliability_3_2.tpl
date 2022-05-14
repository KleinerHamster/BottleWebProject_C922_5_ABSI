% rebase('layout.tpl', title=title, year=year)

<headerHP2>Evaluation of the reliability of the simplest systems by the Monte Carlo method<br></headerHP2>

<form action="/program_mcm_3_2_A" method="post">
    <table border="1" align="center" bordercolor="#bb64a1" cellpadding="5">
       <caption>Probabilities of failure-free operation of elements:</caption>
       <tr>
            <th>A</th>
            <th>B</th>
            <th>C</th>
            <th>D</th>
            <th>E</th>
       </tr>
       <tr>
           <td><input type="text" name="NUMBER_A" size="10" placeholder="0.8" required oninvalid="this.setCustomValidity('Enter the probability of the first element!')" oninput="this.setCustomValidity('')"></td>
           <td><input type="text" name="NUMBER_B" size="10" placeholder="0.9" required oninvalid="this.setCustomValidity('Enter the probability of the second element!')" oninput="this.setCustomValidity('')"></td>
           <td><input type="text" name="NUMBER_C" size="10" placeholder="0.85" required oninvalid="this.setCustomValidity('Enter the probability of the third element!')" oninput="this.setCustomValidity('')"></td>
           <td><input type="text" name="NUMBER_D" size="10" placeholder="0.7" required oninvalid="this.setCustomValidity('Enter the probability of the fourth element!')" oninput="this.setCustomValidity('')"></td>
           <td><input type="text" name="NUMBER_E" size="10" placeholder="0.78" required oninvalid="this.setCustomValidity('Enter the probability of the fifth element!')" oninput="this.setCustomValidity('')"></td>
       </tr>
    </table>

    <pHP>
        <br>Number of tests: <input type="text" step="0.01" size="5" name="NUMBER_N" placeholder="5" required oninvalid="this.setCustomValidity('Enter the number of tests!')" oninput="this.setCustomValidity('')"><br>
    </pHP>

    <p><input type="submit" class="buttonHP" value="Calculate"></p>
</form>

<br><hr class="about">

<pHP>
    Example:
    <br>The system consists of two blocks connected in series. The system fails when at least one block fails. The first block contains three elements: A, B, C (they are connected in parallel) and fails when three elements fail simultaneously. The second one contains two elements D, E and fails when two elements fail simultaneously.
    <br>a) Find by the Monte Carlo method an estimate of P* reliability (probability of failure-free operation) of the system, knowing the probability of failure-free operation of the elements: P(A) = 0.8, P(B)=0.9, P(C)=0.85, P(D)=0.85, P(E)=0.85;
    <br>b) find the absolute error |P-P*| of the found value, where P is the reliability of the system, calculated analytically.
    <br>Perform 100 tests.
    <br><br>Solution:
    <br>a) Using a random number generator, we obtain (or select from special tables of uniformly distributed random numbers) 5 random numbers, for example: 0.97, 0.12, 0.48, 0.22, 0,64; next, we consider that if the random number is less than the probability of the corresponding event, then the event has occurred (the element works flawlessly); if the random number is greater than or equal to the probability of the event, then the event has not occurred (failure).
    <br>We will play the events A, B, C, D, E consisting in the trouble-free operation of the ABC, D, E elements, respectively. We will record the test results in the calculation table. Since P(A)=0.8 and 0.97'!<'0.8, this event did not occur, i.e. element A in this test works with failure. Since P(B)=0.9 and 0.12'<'0.9, this event B has occurred, i.e. element B works flawlessly, etc.
    <br>Thus, two of the three elements of the first block work; therefore, the first block itself works. In the corresponding cells of Table, we put a plus sign.
    <br>If all the events in the block did not occur, i.e. the elements were rejected; in other words, the block, and therefore the entire system, are rejected. In the corresponding cells of Table 1, we put a minus sign.
    <br>The other tests are played out in the same way. The Table shows the results of one hundred tests.
    <br><br>Table:<br>
</pHP>

<iframe width="1150" height="350" frameborder="0" scrolling="no" src="https://onedrive.live.com/embed?resid=2CBF96563B87AD2%21179&authkey=%21AHKo39MSWpRIwAA&em=2&wdAllowInteractivity=False&wdHideGridlines=True&wdHideHeaders=True&wdDownloadButton=True&wdInConfigurator=True&wdInConfigurator=True&edesNext=true&ejss=false"></iframe>

<iframe width="1150" height="550" frameborder="0" scrolling="no" src="https://onedrive.live.com/embed?resid=2CBF96563B87AD2%21184&authkey=%21APGOjYlMM_1LkLk&em=2&wdAllowInteractivity=False&wdHideGridlines=True&wdHideHeaders=True&wdDownloadButton=True&wdInConfigurator=True&wdInConfigurator=True&edesNext=false&ejss=false"></iframe>

<pHP>
    <br>After making 100 tests, we get that in 95 of them the system worked flawlessly. As an estimate of the desired reliability P, we take the relative frequency P *=95/100 = 0.95.
    <br>b) Find the reliability of the system P analytically. The probabilities of failure-free operation of the first and second blocks are equal, respectively:
    <br>P1=1-P(¯A)*P(¯B)*P(¯C)=1-(1-0.8)*(1-0.9)*(1-0.85)=0.997
    <br>P2=1-P(¯C)*P(¯D)=1-(1-0.7)*(1-0.78)=0.934
    <br>Probability of system uptime:
    <br>P=P1*P2=0.997*0.934=0.931
    <br>The required absolute error is equal to:
    <br>|P-P*|=|0.931-0.95|=|-0.019|=0.019
</pHP>