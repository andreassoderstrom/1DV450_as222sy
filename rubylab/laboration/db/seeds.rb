# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)

u1 = User.create(:first_name => "Andreas",
	:last_name => "Soderstrom",
	:email => "andreas@200ok.se",
	:password => "1bralosen")

p1 = Project.create(:name => "Laboration 1",
 :description => "Testing Ruby on rails!",
 :start_date => DateTime.new(2013,2,2,10),
  :end_date => DateTime.new(2013,2,12,10),
   :owner_id => 1  )

s1 = Status.create(:status_name => "Bug")
s1 = Status.create(:status_name => "Fix")