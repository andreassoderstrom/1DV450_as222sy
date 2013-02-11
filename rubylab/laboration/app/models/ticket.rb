class Ticket < ActiveRecord::Base
   attr_accessible :name, :description, :statuses_id, :users_id, :projects_id

  belongs_to :project
  belongs_to :user
  belongs_to :status

end
