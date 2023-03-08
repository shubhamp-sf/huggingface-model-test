from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

tokenizer = AutoTokenizer.from_pretrained("tscholak/cxmefzzi")

model = AutoModelForSeq2SeqLM.from_pretrained("tscholak/cxmefzzi")

promptInput = [
    "What is the total number of clients in the database?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all hotel reservations where the client's username is xyz.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "How many reservations have been made at each hotel?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "What is the name of the hotel with the most reservations?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all clients who have made reservations at the hotel with id 123.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "How many clients have made reservations at the hotel with id 456?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all reservations made by client with id 789.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "What is the average rating for all reservations?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all reservations with a rating of 4 or higher.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "How many reservations were made on date 2022-01-01?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "What is the name of the client with the highest-rated reservation?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all clients with a mobile number that contains the digits 555.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "What is the average age of all clients?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all hotels with a name that contains the word beach.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "How many clients have a username that contains the word hotel?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "What is the total number of reservations made by clients aged 25 or younger?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all reservations made at the hotel with id 789 on date 2022-02-01.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "How many clients have made reservations on the same date as another client?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all clients who have not made any reservations.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "What is the average rating for reservations made by clients over the age of 40?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all hotels where the client with id 555 has made reservations.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "How many clients have the same name as their username?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all reservations made by clients with a mobile number that starts with +1.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "What is the name of the hotel with the fewest reservations?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all clients who have made reservations between dates 2022-01-01 and 2022-01-31.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "How many clients have made reservations with a rating of 3 or lower?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all reservations made at hotels with a name that contains the word resort.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "What is the average age of clients who have made reservations at the hotel with id 321?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all reservations with a rating higher than the average rating.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "How many reservations were made by the client with the highest-rated reservation?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all clients who have made reservations at more than one hotel.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "What is the total number of reservations made at the hotel with id 234?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all clients who have made reservations with a rating of 5.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "How many reservations were made by clients with a username that contains the letter a?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all reservations made by clients aged 30 or older.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "What is the username of the client with the most reservations?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all hotels where the client with id 987 has made reservations with a rating of 4 or higher.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "How many reservations were made on each date?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all clients who have made reservations with a rating higher than the average rating.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "What is the name of the client who made the highest-rated reservation at the hotel with id 456?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all hotels where no reservations have been made.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "How many reservations were made by clients aged 25 to 35?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all clients who have made reservations at a hotel with a name that starts with The.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "What is the name of the hotel with the highest-rated reservation?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all clients who have made reservations for more than three days.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "How many clients have made reservations at more than one hotel?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all reservations made by clients with an odd-numbered id.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "What is the average age of clients who have made reservations with a rating of 4 or higher?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all hotels where no reservations have been made on date 2022-02-01.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "How many reservations were made at hotels with a name that contains the word Grand?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all clients who have made reservations with a rating lower than the average rating.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "What is the name of the client who made the most recent reservation?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all reservations made by clients whose age is a multiple of 10.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "How many clients have a mobile number that contains the digits 123?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all reservations made by clients with a name that starts with A.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "What is the name of the hotel with the highest-rated reservation made on date 2022-01-01?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all clients who have made reservations at hotels with a rating of 4 or higher.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "How many clients have made reservations for dates that are not consecutive?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all hotels where the client with id 555 has made reservations with a rating lower than 3.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "What is the average rating for reservations made by clients under the age of 30?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all reservations made at the hotel with the fewest reservations.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "How many clients have made reservations on date 2022-03-01?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all hotels where the client with id 789 has made reservations with a rating of 5.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "What is the name of the client who made the most reservations?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all clients who have not made reservations at a hotel with a name that contains the word beach.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "How many reservations were made by clients with a mobile number that ends with 5555?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all reservations made by clients with a username that contains the word travel.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "What is the name of the hotel with the highest-rated reservation made by the client with id 123?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all clients who have made reservations at hotels with a name that ends with Inn.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "How many clients have made reservations for dates that are less than a week apart?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all reservations made by clients whose mobile number contains the digits 123 and whose username contains the word hotel.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "What is the name of the hotel with the most reservations made by clients under the age of 30?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all clients who have made reservations with a rating of 1.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "How many clients have made reservations with a dateA before 2022-01-01 and a dateD after 2022-02-01?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all reservations made by clients with a name that contains the word holiday.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "What is the average age of clients who have made reservations at the hotel with the most reservations?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "Show me all clients who have made reservations at hotels with a name that contains the word Palace.| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
    "How many reservations were made by clients with an even-numbered id?| hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age"
]

# prompt | database | table : col1, col2, col3
response = pipeline('text2text-generation', model=model,
                    tokenizer=tokenizer)(promptInput)

print(response)

# started at 7:53pm
# ended around 8:25pm