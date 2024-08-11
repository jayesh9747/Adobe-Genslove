import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from extract_boundaries import ExtractBoundaries
import matplotlib.patches as patches

class CompletingCurve:
    def __init__(self,file_path):
        self.file_path=file_path
        self.get_boundaries()
        
    def rescale_img(self,frame):
        h,w=frame.shape[:2]
        new_h=int(h*0.5)
        new_w=int(w*0.5)
        return cv.resize(frame,(new_h,new_w))
        
    def get_boundaries(self):
        boundaries=ExtractBoundaries(self.file_path)
        self.re_img=boundaries.return_rescale_img()
        self.circle_boundaries=boundaries.get_circle_boundry()
        self.ellipse_boundaries=boundaries.get_ellipse_boundry()
        self.square_boundaries=boundaries.get_square_boundry()
        self.star_boundaries=boundaries.get_star_boundry()
        self.triangle_boundaries=boundaries.get_triangle_boundry()
        
    def regularize_curve(self):
        images = []
        img1=np.zeros_like(self.re_img)
        img2=np.zeros_like(self.re_img)
        
        
        for contour in self.circle_boundaries:
            (x, y), radius = cv.minEnclosingCircle(contour)
            x = int(x)
            y = int(y)
            radius = int(radius)
            
            blank_img = np.zeros_like(self.re_img)
            
            cv.circle(blank_img, (x, y), radius, (0, 255, 0), 2)
            cv.drawContours(blank_img, [contour], -1, (255, 0, 0), 2)
            cv.circle(img1, (x, y), radius, (0, 255, 0), 2)
            cv.drawContours(img2, [contour], -1, (255, 0, 0), 2)
            
            blank_img_rgb = cv.cvtColor(blank_img, cv.COLOR_BGR2RGB)
            
            images.append(blank_img_rgb)
        for contour in self.ellipse_boundaries:
            ellipse = cv.fitEllipse(contour)
            center, (major_axis, minor_axis), angle = ellipse
            
            center = tuple(map(int, center))
            major_axis = int(major_axis)
            minor_axis = int(minor_axis)
            blank_img=np.zeros_like(self.re_img)
            cv.ellipse(blank_img, center, (int(major_axis / 2), int(minor_axis / 2)), angle, 0, 360, (0, 255, 0), 2)
            cv.drawContours(blank_img,[contour],-1,(255,0,0),2)
            cv.ellipse(img1, center, (int(major_axis / 2), int(minor_axis / 2)), angle, 0, 360, (0, 255, 0), 2)
            cv.drawContours(img2,[contour],-1,(255,0,0),2)
            blank_img_rgb = cv.cvtColor(blank_img, cv.COLOR_BGR2RGB)
            images.append(blank_img_rgb)
        
       #Plotting the subplots:
        num_images = len(images)
        fig, axes = plt.subplots(1, num_images, figsize=(15, 5))
        if num_images == 1:
            axes = [axes]
        for i, ax in enumerate(axes):
            ax.imshow(images[i])
            ax.axis('off')  # Hide axes
            legend_patches = [
            patches.Patch(color='blue', alpha=0.5, label='Original Image'),
            patches.Patch(color='green', alpha=0.5, label='Processed Image')]
            ax.legend(handles=legend_patches, loc='upper right')
        
        plt.tight_layout()
        plt.show()

        #Plotting the Final image:
        img1=cv.cvtColor(img1,cv.COLOR_BGR2RGB)
        img2=cv.cvtColor(img2,cv.COLOR_BGR2RGB)
        final_img=[img1,img2]
        fig, axes = plt.subplots(1, len(final_img), figsize=(15, 5))
        if num_images == 1:
            axes = [axes]
        for i, ax in enumerate(axes):
            ax.imshow(final_img[i])
            ax.axis('off')  # Hide axes
            legend_patches = [
            patches.Patch(color='blue', alpha=0.5, label='Original Image'),
            patches.Patch(color='green', alpha=0.5, label='Processed Image')]
            ax.legend(handles=legend_patches, loc='upper right')
        
        plt.tight_layout()
        plt.show()
        
            
    def regularize_line(self):
        line_reg= LineRegularizer()
        for contour in self.star_boundaries:
            d=[contour]
            data=[d]
            img_path=line_reg.get_regularize_line_img(data)
            
        for contour in self.square_boundaries:
            d=[contour]
            data=[d]
            img_path=line_reg.get_regularize_line_img(data)
                
                
            
            
            
        
        
        
        
    





