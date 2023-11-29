Author: Dylan Murphy

Contact: dmurphy6@uoregon.edu

Description: This is a checkpoint calculator for brevet bike races. It follows the table: 
| Control Location (km) | Minimum Speed (km/hr) | Maximum Speed (km/hr) |
|-----------------------|-----------------------|-----------------------|
| 0 - 200               | 15                    | 34                    |
| 200 - 400             | 15                    | 32                    |
| 400 - 600             | 15                    | 30                    |
| 600 - 1000            | 11.428                | 28                    |

and has a special case for checkpoints within the first 60km where the close time is a 20 km/hr minimum speed + 1 hr. The maximum distance for the last checkpoint is 120% the brevet distance and if you type in a number that exceeds that it will automatically default to 120% * the brevet distance. The page updates as you type in values without reloading the page by using AJAX. 

There are also two buttons, "Submit" and "Display"
Submit will save the current data in the table to a database and clear the table after doing so.
Display will fetch that data from the database and display it in the table.

To run this, get in the "project-5" directory and run the following command:

docker compose up

to stop it type

docker compose down