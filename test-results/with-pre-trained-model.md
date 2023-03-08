<table>
  <tbody>
    <tr>
      <td>
        <div>Prompt</div>
      </td>
      <td>
        <div>SQL Query</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>What is the total number of clients in the database?</div>
      </td>
      <td>
        <div>select count(*) from client</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all hotel reservations where the client's username is xyz.</div>
      </td>
      <td>
        <div>select t2.type from client as t1 join reservation as t2 on t1.id = t2.clientId where t1.username = "xyz"</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>How many reservations have been made at each hotel?</div>
      </td>
      <td>
        <div>select t1.name, count(*) from hotel as t1 join reservation as t2 on t1.id = t2.clientId group by t1.id</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>What is the name of the hotel with the most reservations?</div>
      </td>
      <td>
        <div>select t2.name from reservation as t1 join hotel as t2 on t1.hotelId = t2.id group by t1.hotelId order by count(*) desc limit 1</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all clients who have made reservations at the hotel with id 123.</div>
      </td>
      <td>
        <div>select distinct t1.name from client as t1 join reservation as t2 on t1.id = t2.clientId where t2.hotelId = 123</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>How many clients have made reservations at the hotel with id 456?</div>
      </td>
      <td>
        <div>select count(distinct clientId) from reservation where hotelId = 456</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all reservations made by client with id 789.</div>
      </td>
      <td>
        <div>select clientId from reservation where clientId = 789</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>What is the average rating for all reservations?</div>
      </td>
      <td>
        <div>select avg(rating) from reservation</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all reservations with a rating of 4 or higher.</div>
      </td>
      <td>
        <div>select * from reservation where rating &gt;= 4</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>How many reservations were made on date 2022-01-01?</div>
      </td>
      <td>
        <div>select count(*) from reservation where checkInDate = "2022-01-01"</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>What is the name of the client with the highest-rated reservation?</div>
      </td>
      <td>
        <div>select t1.name from client as t1 join reservation as t2 on t1.id = t2.clientId order by t2.rating desc limit 1</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all clients with a mobile number that contains the digits 555.</div>
      </td>
      <td>
        <div>select name from client where telephone like "%555%"</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>What is the average age of all clients?</div>
      </td>
      <td>
        <div>select avg(age) from client</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all hotels with a name that contains the word beach.</div>
      </td>
      <td>
        <div>select name from hotel where name like '%beach%'</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>How many clients have a username that contains the word hotel?</div>
      </td>
      <td>
        <div>select count(*) from client where username like "%hotel%"</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>What is the total number of reservations made by clients aged 25 or younger?</div>
      </td>
      <td>
        <div>select count(*) from reservation as t1 join client as t2 on t1.clientId = t2.id where t2.age &lt;= 25</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all reservations made at the hotel with id 789 on date 2022-02-01.</div>
      </td>
      <td>
        <div>select * from reservation where hotelId = 789 and checkInDate = "2022-02-01"</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>How many clients have made reservations on the same date as another client?</div>
      </td>
      <td>
        <div>select count(distinct clientId) from reservation where checkInDate = (select checkInDate from reservation)</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all clients who have not made any reservations.</div>
      </td>
      <td>
        <div>select name from client where id not in (select clientId from reservation)</div>
      </td>
	</tr>
    <tr>
      <td>
        <div>What is the average rating for reservations made by clients over the age of 40?</div>
      </td>
      <td>
        <div>select avg(t2.rating) from client as t1 join reservation as t2 on t1.id = t2.clientId where t1.age &gt; 40</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all hotels where the client with id 555 has made reservations.</div>
      </td>
      <td>
        <div>select distinct t2.name from reservation as t1 join hotel as t2 on t1.hotelId = t2.id join client as t3 on t1.clientId = t3.id where t3.id = 555</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>How many clients have the same name as their username?</div>
      </td>
      <td>
        <div>select count(*) from client where name = username</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all reservations made by clients with a mobile number that starts with +1.</div>
      </td>
      <td>
        <div>select clientId from reservation where clientId like '+1'</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>What is the name of the hotel with the fewest reservations?</div>
      </td>
      <td>
        <div>select t2.name from reservation as t1 join hotel as t2 on t1.hotelId = t2.id group by t1.hotelId order by count(*) asc limit 1</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all clients who have made reservations between dates 2022-01-01 and 2022-01-31.</div>
      </td>
      <td>
        <div>select t1.name from client as t1 join reservation as t2 on t1.id = t2.clientId where t2.checkInDate &gt;= "2022-01-01" and t2.checkOutDate &lt;= "2022-01-31"</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>How many clients have made reservations with a rating of 3 or lower?</div>
      </td>
      <td>
        <div>select count(distinct clientId) from reservation where rating &lt;= 3</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all reservations made at hotels with a name that contains the word resort.</div>
      </td>
      <td>
        <div>select t1.type from reservation as t1 join hotel as t2 on t1.hotelId = t2.id where t2.name like '%resort%'</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>What is the average age of clients who have made reservations at the hotel with id 321?</div>
      </td>
      <td>
        <div>select avg(t1.age) from client as t1 join reservation as t2 on t1.id = t2.clientId where t2.hotelId = 321</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all reservations with a rating higher than the average rating.</div>
      </td>
      <td>
        <div>select distinct rating from reservation where rating &gt; (select avg(rating) from reservation)</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>How many reservations were made by the client with the highest-rated reservation?</div>
      </td>
      <td>
        <div>select count(*) from reservation where clientId = (select clientId from reservation order by rating desc limit 1)</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all clients who have made reservations at more than one hotel.</div>
      </td>
      <td>
        <div>select clientId from reservation group by clientId having count(*) &gt; 1</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>What is the total number of reservations made at the hotel with id 234?</div>
      </td>
      <td>
        <div>select count(*) from reservation where hotelId = 234</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all clients who have made reservations with a rating of 5.</div>
      </td>
      <td>
        <div>select distinct t1.name from client as t1 join reservation as t2 on t1.id = t2.clientId where t2.rating = 5</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>How many reservations were made by clients with a username that contains the letter a?</div>
      </td>
      <td>
        <div>select count(*) from reservation as t1 join client as t2 on t1.clientId = t2.id where t2.username like '%a%'</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all reservations made by clients aged 30 or older.</div>
      </td>
      <td>
        <div>select distinct t2.type from client as t1 join reservation as t2 on t1.id = t2.clientId where t1.age &gt;= 30</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>What is the username of the client with the most reservations?</div>
      </td>
      <td>
        <div>select t1.name from client as t1 join reservation as t2 on t1.id = t2.clientId group by t1.id order by count(*) desc limit 1</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all hotels where the client with id 987 has made reservations with a rating of 4 or higher.</div>
      </td>
      <td>
        <div>select distinct t2.name from reservation as t1 join hotel as t2 on t1.hotelId = t2.id join client as t3 on t1.clientId = t3.id where t3.rating &gt;= 4 and t3.id = 987</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>How many reservations were made on each date?</div>
      </td>
      <td>
        <div>select checkInDate, checkOutDate, count(*) from reservation group by checkInDate, checkOutDate</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all clients who have made reservations with a rating higher than the average rating.</div>
      </td>
      <td>
        <div>select distinct t1.name from client as t1 join reservation as t2 on t1.id = t2.clientId where t2.rating &gt; (select avg(rating) from reservation)</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>What is the name of the client who made the highest-rated reservation at the hotel with id 456?</div>
      </td>
      <td>
        <div>select t1.name from client as t1 join reservation as t2 on t1.id = t2.clientId where t2.hotelId = 456 order by t2.rating desc limit 1</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all hotels where no reservations have been made.</div>
      </td>
      <td>
        <div>select name from hotel where id not in (select hotelId from reservation)</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>How many reservations were made by clients aged 25 to 35?</div>
      </td>
      <td>
        <div>select count(*) from client as t1 join reservation as t2 on t1.id = t2.clientId where t1.age between 25 and 35</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all clients who have made reservations at a hotel with a name that starts with The.</div>
      </td>
      <td>
        <div>select t1.name from client as t1 join reservation as t2 on t1.id = t2.clientId join hotel as t3 on t2.hotelId = t3.id where t3.name like '% the %'</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>What is the name of the hotel with the highest-rated reservation?</div>
      </td>
      <td>
        <div>select t2.name from reservation as t1 join hotel as t2 on t1.hotelId = t2.id order by t1.rating desc limit 1</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all clients who have made reservations for more than three days.</div>
      </td>
      <td>
        <div>select t1.name from client as t1 join reservation as t2 on t1.id = t2.clientId where t2.checkoutDate &gt; 3</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>How many clients have made reservations at more than one hotel?</div>
      </td>
      <td>
        <div>select count(distinct clientId) from reservation group by clientId having count(distinct hotelId) &gt; 1</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all reservations made by clients with an odd-numbered id.</div>
      </td>
      <td>
        <div>select clientId from reservation where clientId not in (select clientId from client where clientId = 2)</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>What is the average age of clients who have made reservations with a rating of 4 or higher?</div>
      </td>
      <td>
        <div>select avg(t1.age) from client as t1 join reservation as t2 on t1.id = t2.clientId where t2.rating &gt;= 4</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all hotels where no reservations have been made on date 2022-02-01.</div>
      </td>
      <td>
        <div>select name from hotel except select t2.name from reservation as t1 join hotel as t2 on t1.hotelId = t2.id where t1.checkInDate = "2022-02-01"</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>How many reservations were made at hotels with a name that contains the word Grand?</div>
      </td>
      <td>
        <div>select count(*) from reservation as t1 join hotel as t2 on t1.hotelId = t2.id where t2.name like "%grand%"</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all clients who have made reservations with a rating lower than the average rating.</div>
      </td>
      <td>
        <div>select distinct t1.name from client as t1 join reservation as t2 on t1.id = t2.clientId where t2.rating &lt; (select avg(rating) from reservation)</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>What is the name of the client who made the most recent reservation?</div>
      </td>
      <td>
        <div>select t1.name from client as t1 join reservation as t2 on t1.id = t2.clientId order by t2.checkInDate desc limit 1</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all reservations made by clients whose age is a multiple of 10.</div>
      </td>
      <td>
        <div>select t2.type from client as t1 join reservation as t2 on t1.id = t2.clientId where t1.age &gt; 10</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>How many clients have a mobile number that contains the digits 123?</div>
      </td>
      <td>
        <div>select count(*) from client where telephone like "%123"</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all reservations made by clients with a name that starts with A.</div>
      </td>
      <td>
        <div>select t2.type from client as t1 join reservation as t2 on t1.id = t2.clientId where t1.name like 'A%'</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>What is the name of the hotel with the highest-rated reservation made on date 2022-01-01?</div>
      </td>
      <td>
        <div>select t2.name from reservation as t1 join hotel as t2 on t1.hotelId = t2.id where t1.checkInDate = "2022-01-01" order by t1.rating desc limit 1</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all clients who have made reservations at hotels with a rating of 4 or higher.</div>
      </td>
      <td>
        <div>select distinct t1.name from client as t1 join reservation as t2 on t1.id = t2.clientId where t2.rating &gt;= 4</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>How many clients have made reservations for dates that are not consecutive?</div>
      </td>
      <td>
        <div>select count(distinct clientId) from reservation where checkInDate, checkOutDate not consecutive</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all hotels where the client with id 555 has made reservations with a rating lower than 3.</div>
      </td>
      <td>
        <div>select t2.name from reservation as t1 join hotel as t2 on t1.hotelId = t2.id join client as t3 on t1.clientId = t3.id where t3.rating &lt; 3 and t3.id = 555</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>What is the average rating for reservations made by clients under the age of 30?</div>
      </td>
      <td>
        <div>select avg(t2.rating) from client as t1 join reservation as t2 on t1.id = t2.clientId where t1.age &lt; 30</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all reservations made at the hotel with the fewest reservations.</div>
      </td>
      <td>
        <div>select t1.type from reservation as t1 join hotel as t2 on t1.hotelId = t2.id group by t1.hotelId order by count(*) asc limit 1</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>How many clients have made reservations on date 2022-03-01?</div>
      </td>
      <td>
        <div>select count(distinct clientId) from reservation where checkInDate = "2022-03-01"</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all hotels where the client with id 789 has made reservations with a rating of 5.</div>
      </td>
      <td>
        <div>select t2.name from reservation as t1 join hotel as t2 on t1.hotelId = t2.id join client as t3 on t1.clientId = t3.id where t3.rating = 5 and t3.id = 789</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>What is the name of the client who made the most reservations?</div>
      </td>
      <td>
        <div>select t1.name from client as t1 join reservation as t2 on t1.id = t2.clientId group by t1.id order by count(*) desc limit 1</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all clients who have not made reservations at a hotel with a name that contains the word beach.</div>
      </td>
      <td>
        <div>select name from client except select t1.name from client as t1 join reservation as t2 on t1.id = t2.clientId join hotel as t3 on t2.hotelId = t3.id where t3.name like "%beach%"</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>How many reservations were made by clients with a mobile number that ends with 5555?</div>
      </td>
      <td>
        <div>select count(*) from reservation as t1 join client as t2 on t1.clientId = t2.id where t2.telephone like "%555"</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all reservations made by clients with a username that contains the word travel.</div>
      </td>
      <td>
        <div>select t2.type from client as t1 join reservation as t2 on t1.id = t2.clientId where t1.name like '%travel%'</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>What is the name of the hotel with the highest-rated reservation made by the client with id 123?</div>
      </td>
      <td>
        <div>select t2.name from reservation as t1 join hotel as t2 on t1.hotelId = t2.id where t1.clientId = 123 order by t1.rating desc limit 1</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all clients who have made reservations at hotels with a name that ends with Inn.</div>
      </td>
      <td>
        <div>select t1.name from client as t1 join reservation as t2 on t1.id = t2.clientId join hotel as t3 on t2.hotelId = t3.id where t3.name like 'Inn%'</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>How many clients have made reservations for dates that are less than a week apart?</div>
      </td>
      <td>
        <div>select count(distinct clientId) from reservation where checkInDate &lt; 7 days</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all reservations made by clients whose mobile number contains the digits 123 and whose username contains the word hotel.</div>
      </td>
      <td>
        <div>select t2.type from client as t1 join reservation as t2 on t1.id = t2.clientId where t1.name like '%123%' intersect select t2.type from client as t1 join reservation as t2 on t1.id = t2.clientId where t1.name like '%hotel%'</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>What is the name of the hotel with the most reservations made by clients under the age of 30?</div>
      </td>
      <td>
        <div>select t2.name from reservation as t1 join hotel as t2 on t1.hotelId = t2.id join client as t3 on t1.clientId = t3.id where t3.age &lt; 30 group by t1.hotelId order by count(*) desc limit 1</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all clients who have made reservations with a rating of 1.</div>
      </td>
      <td>
        <div>select distinct t1.name from client as t1 join reservation as t2 on t1.id = t2.clientId where t2.rating = 1</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>How many clients have made reservations with a dateA before 2022-01-01 and a dateD after 2022-02-01?</div>
      </td>
      <td>
        <div>select count(distinct clientId) from reservation where checkInDate &lt; 2022-01-01 intersect select count(distinct clientId) from reservation where checkOutDate &gt; 2022-02-01</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all reservations made by clients with a name that contains the word holiday.</div>
      </td>
      <td>
        <div>select t2.type from client as t1 join reservation as t2 on t1.id = t2.clientId where t1.name like '%holiday%'</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>What is the average age of clients who have made reservations at the hotel with the most reservations?</div>
      </td>
      <td>
        <div>select avg(t1.age) from client as t1 join reservation as t2 on t1.id = t2.clientId group by t2.hotelId order by count(*) desc limit 1</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>Show me all clients who have made reservations at hotels with a name that contains the word Palace.</div>
      </td>
      <td>
        <div>select t1.name from client as t1 join reservation as t2 on t1.id = t2.clientId join hotel as t3 on t2.hotelId = t3.id where t3.name like "%palace%"</div>
      </td>
    </tr>
    <tr>
      <td>
        <div>How many reservations were made by clients with an even-numbered id?</div>
      </td>
      <td>
        <div>select count(*) from reservation where clientId = 2</div>
      </td>
    </tr>
  </tbody>
</table>
