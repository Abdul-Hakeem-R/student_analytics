step 1: Copy the project folder
step 2: Create a virtual environment and Acctivate it
step 3: Create db and update it in setting.py
step 4: Run Migrations
step 5: Create Admin
step 6: Import Students and Import Test(Inserting Manually takes lots od time)
step 7:  API Endpoints
Method	Endpoint	Description
POST	        /api/upload/	                            Upload CSV results
GET         	/api/students/{student_id}/performance/	    Get student performance
GET	            /api/subjects/{subject_id}/analytics/	    Get subject analytics
GET	            /api/tests/{test_id}/leaderboard/	        Get leaderboard for test

