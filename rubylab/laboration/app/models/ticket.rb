class Ticket < ActiveRecord::Base
   attr_accessible :name, :description, :status_id, :user_id, :project_id

  belongs_to :project
  belongs_to :user
  belongs_to :status

end
