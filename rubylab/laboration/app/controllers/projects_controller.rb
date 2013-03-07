class ProjectsController < ApplicationController
	before_filter :authenticate
	before_filter :is_owner, only: [:edit, :destroy, :update]
	before_filter :is_member, only: [:show]
	def index
		@projects = Project.search(params[:search])
		@users = User.all
		@user = User.find(session[:user_id])
	end

	def show
		@users = Project.find(params[:id]).users
		@project = Project.find(params[:id])
		@tickets = Project.find(params[:id]).tickets
		session[:project_id] = params[:id]
	end

	def new
		@project = Project.new
		@users = User.all
	end

	def create
		@users = User.all
		@project = Project.new(params[:project])
		@project.owner_id = session[:user_id]
		#call updateprojectusers

		if params[:user_ids] != nil
			updateProjectUsers
		
		
			if @project.save
				redirect_to project_path(@project)
			else
				
				render :action => "new"

			end
		else
			render :action => "new"
		end
	end

	def updateProjectUsers
		@project.users.delete(@project.users)
		

		params[:user_ids].each do |u|
			user = User.find(u)
			unless @project.users.include?(user)
				@project.users << user
			end
		end
	end




	def edit 
		@project = Project.find(params[:id])
		@users = User.all
		
	end

	def update
		@users = User.all
		@project = Project.find(params[:id])
		updateProjectUsers
		if @project.update_attributes(params[:project])
			redirect_to project_path
		else
			render :action => "edit"
		end
	end

	def destroy
		@project = Project.find(params[:id])
		@project.destroy
		redirect_to projects_path
	end


	

end
