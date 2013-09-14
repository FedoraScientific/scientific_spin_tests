package demo;

import org.apache.commons.math3.stat.descriptive.DescriptiveStatistics;

public class DescriptiveStatsDemo {

	public static void main(String[] args) {
		 // Get a DescriptiveStatistics instance
        DescriptiveStatistics stats = new DescriptiveStatistics();

        // Add the data from the array
        for( int i = 0; i < 100; i++){
            stats.addValue(i);
        }

        // Compute some statistics
        double mean = stats.getMean();
        double std = stats.getStandardDeviation();
        double median = stats.getPercentile(50);
        
        System.out.println(mean);
        System.out.println(median);
        System.out.println(std);

    }
}


	
