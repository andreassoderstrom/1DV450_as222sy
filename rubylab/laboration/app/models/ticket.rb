class Ticket < ActiveRecord::Base
  attr_accessible :name, :description, :status_id, :user_id, :project_id


	validates	:name,
				:presence => {:message => "Name field cannot be empty"},
				:length => {:minimum => 3, :message => "Your ticket name needs to contain atleast 3 letters"}

	validates	:description,
				:presence => {:message => "Your ticket needs a description"}



  belongs_to :project
  belongs_to :user
  belongs_to :status

end
