class User < ActiveRecord::Base
   has_secure_password
   attr_accessible :first_name, :last_name, :email, :password, :body

   has_and_belongs_to_many :projects
   has_many :tickets

   def self.authenticate(user, password)
   	user.try(:authenticate, password)
   end
end
