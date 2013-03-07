class Project < ActiveRecord::Base
	attr_accessible :name, :description, :start_date, :end_date, :owner_id, :body

	has_many :tickets, :dependent => :destroy
	has_and_belongs_to_many :users


	validates	:name,
				:presence => {:message => "Name field cannot be empty"},
				:length => {:minimum => 3, :message => "Your project name needs to contain atleast 3 letters"}

	validates	:description,
				:presence => {:message => "Your project needs a description"}

	validate	:validate_date

	def validate_date
		if end_date && start_date
      		errors.add(:end_date, "Felaktikt slutdatum") if end_date < start_date
    	end
	end
	
	def self.search(search)
		if search
			find(:all, :conditions => ['name LIKE ? OR description LIKE ?', "%#{search}%", "%#{search}%"])
		else
			find(:all)
		end
	end

end
