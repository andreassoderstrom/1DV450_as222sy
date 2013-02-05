class Project < ActiveRecord::Base
  attr_accessible :name, :description, :start_date, :end_date, :owner_id, :body
end
