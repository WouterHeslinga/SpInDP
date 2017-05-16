using System;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata;

namespace idpSpin.Models
{
    public partial class SpinContext : DbContext
    {
        public virtual DbSet<Spin> Spin { get; set; }

        public SpinContext(DbContextOptions<SpinContext> options) : base(options) { }
        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Spin>(entity =>
            {
                entity.Property(e => e.GeluidSensor).HasMaxLength(40);

                entity.Property(e => e.HellingSensor).HasMaxLength(30);

                entity.Property(e => e.Servo1).HasMaxLength(40);

                entity.Property(e => e.Servo10).HasMaxLength(40);

                entity.Property(e => e.Servo11).HasMaxLength(40);

                entity.Property(e => e.Servo12).HasMaxLength(40);

                entity.Property(e => e.Servo13).HasMaxLength(40);

                entity.Property(e => e.Servo14).HasMaxLength(40);

                entity.Property(e => e.Servo15).HasMaxLength(40);

                entity.Property(e => e.Servo16).HasMaxLength(40);

                entity.Property(e => e.Servo17).HasMaxLength(40);

                entity.Property(e => e.Servo18).HasMaxLength(40);

                entity.Property(e => e.Servo2).HasMaxLength(40);

                entity.Property(e => e.Servo3).HasMaxLength(40);

                entity.Property(e => e.Servo4).HasMaxLength(40);

                entity.Property(e => e.Servo5).HasMaxLength(40);

                entity.Property(e => e.Servo6).HasMaxLength(40);

                entity.Property(e => e.Servo7).HasMaxLength(40);

                entity.Property(e => e.Servo8).HasMaxLength(40);

                entity.Property(e => e.Servo9).HasMaxLength(40);

                entity.Property(e => e.Tijd).HasMaxLength(40);
            });
        }
    }
}